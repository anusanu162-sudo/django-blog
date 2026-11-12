import logging

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ContactForm
from .models import AboutUs, Post

logger = logging.getLogger("testing")


def index(request):
    blog_title = "Latest Posts"
    query = request.GET.get("q", "").strip()

    all_posts = Post.objects.order_by("-created_at")
    if query:
        all_posts = all_posts.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(category__name__icontains=query)
        )

    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "index.html",
        {"blog_title": blog_title, "page_obj": page_obj, "query": query},
    )


def detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id).order_by("-created_at")
    except Post.DoesNotExist:
        raise Http404("Post does not exist.")
    return render(request, "detail.html", {"post": post, "related_posts": related_posts})


def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))


def new_url_view(request):
    return HttpResponse("This is the new URL")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            logger.debug("Contact message saved from %s", form.cleaned_data["email"])
            return render(
                request,
                "contact.html",
                {
                    "form": ContactForm(),
                    "success_message": "Thanks! Your message has been received.",
                },
            )
        logger.debug("Contact form validation failed.")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


def about(request):
    about_record = AboutUs.objects.first()
    about_content = (
        about_record.content
        if about_record
        else "About us content has not been added yet."
    )
    return render(request, "about.html", {"about_content": about_content})
