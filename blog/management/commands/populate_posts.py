from typing import Any

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from blog.models import Category, Post


class Command(BaseCommand):
   help = "This command inserts post data"

   def handle(self, *args: Any, **options: Any):
      Post.objects.all().delete()

      posts = [
         (
            "The Future of AI",
            "Technology",
            "Artificial intelligence is already part of everyday life, from search results and "
            "recommendations to medical imaging and fraud detection. Modern systems learn patterns "
            "from large amounts of data instead of following hand-written rules. The next decade "
            "will be shaped by how well we handle accuracy, privacy, and the jobs these tools "
            "change. Understanding the basics helps you judge both the hype and the real benefits.",
         ),
         (
            "Exploring the Cosmos",
            "Science",
            "The universe is roughly 13.8 billion years old, and everything we can see is a tiny "
            "fraction of it. Telescopes such as Hubble and James Webb read light that left distant "
            "galaxies billions of years ago, so looking out is also looking back in time. Nebulae "
            "like the Tarantula are stellar nurseries where new stars are born. Every observation "
            "adds another piece to the map of where we are.",
         ),
         (
            "Healthy Living Tips",
            "Health",
            "Small, repeatable habits matter far more than short bursts of effort. Filling half "
            "your plate with vegetables and fruit is one of the simplest changes you can make. Aim "
            "for regular sleep, a short daily walk, and water instead of sugary drinks. "
            "Consistency beats intensity: a routine you can keep for months will always outperform "
            "a strict plan you abandon in a week.",
         ),
         (
            "The Art of Coding",
            "Technology",
            "Writing code is mostly reading and thinking; typing is the smallest part. Clear names, "
            "small functions, and short comments explain intent better than clever tricks. Version "
            "control lets you experiment safely and see why a change was made. Treat every bug as "
            "information and every code review as free training, and the craft improves faster than "
            "any tutorial can teach.",
         ),
         (
            "Traveling on a Budget",
            "Travel",
            "Travel costs are decided long before you pack. Booking weeks ahead, flying midweek, "
            "and travelling outside peak season usually saves the most. Hostels, guesthouses, and "
            "simple local restaurants cut daily costs without cutting the experience. Carry a small "
            "buffer for surprises and keep the plan flexible, because the cheapest route is often "
            "the one you discover after you arrive.",
         ),
         (
            "Mindfulness in Daily Life",
            "Lifestyle",
            "Mindfulness is paying attention to the present moment without judging it. It does not "
            "need a cushion or an hour of silence; three slow breaths before a meeting counts. "
            "Noticing what you feel, what you hear, and what you are about to do creates a small gap "
            "between impulse and action. Practised daily, that gap is where calmer decisions come "
            "from.",
         ),
         (
            "The Rise of Remote Work",
            "Career",
            "Remote work moved from perk to expectation in a few short years. It widens hiring, "
            "removes commutes, and gives people control over their environment. It also blurs the "
            "line between office and home, so clear working hours and a dedicated space matter. "
            "Teams that write things down and communicate asynchronously tend to do better than "
            "those that depend on being in the same room.",
         ),
         (
            "Climate Change and Us",
            "Science",
            "The climate is changing because burning fossil fuels adds greenhouse gases faster than "
            "natural systems can absorb them. The effects are already visible: hotter summers, "
            "heavier rainfall, and rising sea levels. Renewables such as wind and solar are now "
            "among the cheapest sources of new electricity. Individual choices help, but policy, "
            "grid upgrades, and efficiency at scale decide how quickly emissions fall.",
         ),
         (
            "Learning a New Language",
            "Education",
            "Adults can learn languages well; they just need regular contact rather than perfect "
            "conditions. Fifteen focused minutes a day beats a three-hour session once a month. "
            "Learn phrases you will actually use, speak out loud even when you are alone, and "
            "accept mistakes as part of the process. Spaced repetition handles vocabulary, while "
            "real conversation builds the confidence no app can give you.",
         ),
         (
            "The Joy of Reading",
            "Culture",
            "Reading is a skill that deepens with practice. A few pages a day builds the habit "
            "faster than waiting for a free weekend. Keep a book where you already sit, and let "
            "yourself abandon titles that do not hold you. Reading widely builds vocabulary, "
            "patience, and empathy, because every book is a chance to see the world through someone "
            "else's eyes.",
         ),
         (
            "Fitness Myths Debunked",
            "Health",
            "Soreness is not proof of progress, and sweat is not a measure of effort. Spot "
            "reduction does not exist: training your abs will not remove belly fat. Rest days are "
            "when muscles actually adapt, so recovery is part of the programme. The best routine is "
            "one you can repeat three times a week, built on steady progression and good form.",
         ),
         (
            "The World of Cryptocurrency",
            "Finance",
            "Cryptocurrency is digital money recorded on a blockchain, a ledger copied across many "
            "computers. No single authority approves transactions; network rules and consensus do. "
            "That makes transfers possible without a bank, but it also means mistakes are usually "
            "permanent and prices can swing sharply. Anyone entering should understand custody, "
            "fees, and the risk of losing keys before investing anything.",
         ),
         (
            "Sustainable Fashion",
            "Lifestyle",
            "Fashion's biggest impact comes from how much we buy and how quickly we discard it. "
            "Choosing second-hand, repairing what you already own, and washing less often reduces "
            "waste with almost no effort. Natural fibres are not automatically better; longevity "
            "matters more than the label. Buying fewer, better pieces and wearing them for years is "
            "the most sustainable choice available.",
         ),
         (
            "Space Exploration Milestones",
            "Science",
            "Spaceflight moved from a Cold War race to routine launches in under seventy years. "
            "Sputnik opened the era in 1957, Apollo 11 put people on the Moon in 1969, and reusable "
            "rockets have since cut the cost of reaching orbit. Rovers now study Mars directly, "
            "while probes have visited every planet in the solar system. Each milestone built the "
            "technology for the next.",
         ),
         (
            "The Psychology of Habits",
            "Lifestyle",
            "Habits form through a loop: a cue, a routine, and a reward. Because the brain automates "
            "whatever it repeats, the easiest way to change behaviour is to change the cue or the "
            "environment, not your willpower. Make good habits obvious and one step easier; make "
            "unwanted ones awkward and out of reach. Track the streak, and expect to miss "
            "occasionally without quitting.",
         ),
         (
            "Digital Detox Challenge",
            "Lifestyle",
            "Constant notifications train the brain to check for updates even when nothing is "
            "happening. A short detox is less about quitting technology and more about noticing how "
            "you use it. Turn off non-essential alerts, keep the phone out of the bedroom, and set "
            "a screen-free hour each day. Most people find their attention comes back within a "
            "week.",
         ),
         (
            "Cooking with Fresh Herbs",
            "Food",
            "Fresh herbs add flavour that dried ones cannot match. Delicate leaves like basil and "
            "parsley go in at the end of cooking, while rosemary and thyme can simmer from the "
            "start. Wash and dry them well so they do not steam, then add them to salads, eggs, "
            "soups, and dressings. A few pots on a windowsill will keep you supplied for months.",
         ),
         (
            "The Evolution of Music",
            "Culture",
            "Music has always followed technology. Sheet music made compositions portable, the "
            "phonograph made performance repeatable, and radio made it free. Vinyl, cassettes, CDs, "
            "and streaming each changed how music was packaged and sold. What has not changed is "
            "the reason people listen: rhythm, memory, and the feeling of being understood by a "
            "song.",
         ),
         (
            "Personal Finance Basics",
            "Finance",
            "Financial security starts with knowing where money goes. Track your spending for one "
            "month, then build a budget around essentials, savings, and a small amount for fun. "
            "Keep an emergency fund covering three to six months of expenses before investing. Pay "
            "off high-interest debt first, automate your savings, and let compound interest do the "
            "work over time.",
         ),
         (
            "The Power of Networking",
            "Career",
            "Networking is not collecting contacts; it is building relationships before you need "
            "them. Ask questions, listen properly, and remember what people care about. Offer help "
            "where you can, because reciprocity is what keeps a network alive. A small group of "
            "people who trust your work will open more doors than a thousand names in a "
            "spreadsheet.",
         ),
      ]

      for title, category_name, content in posts:
          category = Category.objects.get(name=category_name)
          Post.objects.create(
              title=title,
              content=content,
              image_url=f"/static/images/posts/{slugify(title)}.jpg",
              category=category,
          )
      self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))
