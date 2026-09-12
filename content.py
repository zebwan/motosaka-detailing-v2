# -*- coding: utf-8 -*-
"""
Motosaka Detailing — all site content in one place.
Edit values here, then run:  python3 build.py
"""

BRAND = {
    "name": "MOTOSAKA",
    "full": "MOTOSAKA Detailing",
    "tagline": "Auto Detailing",
    "phone_display": "+60 12-405 8765",
    "phone_raw": "60124058765",
    "email": "motosakadetailing@gmail.com",
    "address_l1": "92 Jalan Utama 26, Taman Mutiara Rini",
    "address_l2": "81300 Skudai, Johor Bahru",
    "address_l3": "Malaysia",
    "wa_text": "Hi Motosaka, I'd like to book an appointment for my bike.",
    "title": "MOTOSAKA Detailing — Premium Motorcycle Detailing in Johor Bahru",
    "description": ("Refined detailing, paint correction and restoration for motorcycles in Johor Bahru. "
                    "Thoughtful care, a sharper finish, and a polished presentation from wash to restoration."),
}

NAV = [
    ("Work", "#work"),
    ("Process", "#process"),
    ("Packages", "#packages"),
    ("Reviews", "#reviews"),
    ("FAQ", "#faq"),
    ("Contact", "#contact"),
]

HERO = {
    "slogan_1": "You ride,",
    "slogan_2": "we refine.",
    # words wrapped in * render in the accent (white) weight
    "headline": "— Refined care for *bikes* of *distinction*.",
    "cta_title": "See the standard",
    "cta_sub": "Appointment-only, so every bike gets the time it needs.",
    "cta_label": "Book Appointment",
    "stats": [
        ("5.0", "", "Google rating", "From riders across Johor"),
        ("RM50", "", "Starting price", "Premium Plus+ upkeep"),
    ],
    "card_title": "Signature Treatment",
    "card_sub": "// Most requested",
    "card_video": "assets/video/reel2.mp4",
}

INTRO = ("Quiet precision, considered care, and a finish that speaks for itself. "
         "MOTOSAKA Detailing is built for riders who value finish, condition, and quiet "
         "attention to detail. Every appointment is handled with a more deliberate approach, "
         "allowing each motorcycle to leave cleaner, sharper, and unmistakably better kept.")

# ---------------------------------------------------------------- 001 WORK
WORK = {
    "label": "Our Work",
    "index": "001",
    "headline": "A closer look at the finish.",
    "body": ("Selected details, completed work, and the kind of presentation "
             "riders notice immediately in person."),
    "note": "Every bike is photographed after handover, never staged before the work is done.",
    "counter": "19 / 19",
    "feature": {
        "kicker": "Featured Work",
        "title": "Level 3 Correction",
        "body": ("Three-stage paint correction with engine bay detailing. Targets swirls, "
                 "marks and light scratching for roughly 80% to 95% correction."),
        "img": "assets/img/gallery5.webp",
    },
    "wide": {
        "kicker": "The Standard",
        "title": "Measured work, better-kept rides",
        "body": ("A complete system of treatments that adapt to the condition and "
                 "character of the motorcycle in front of us."),
        "img": "assets/img/gallery12.webp",
    },
    "tiles": [
        ("Wheels & Forks", "assets/img/gallery1.webp"),
        ("Engine Bay", "assets/img/gallery3.webp"),
        ("Paintwork", "assets/img/gallery9.webp"),
        ("Metalwork", "assets/img/gallery11.webp"),
        ("Cockpit", "assets/img/gallery16.webp"),
        ("Finish", "assets/img/gallery18.webp"),
    ],
    "marquee": "Appointment-only detailing in Johor Bahru",
    "cta": ("View the full gallery", "#work"),
}

# ------------------------------------------------------------- 002 PROCESS
PROCESS = {
    "label": "Our Process",
    "index": "002",
    "headline": "A more deliberate process.",
    "body": ("Each appointment begins with the condition of the bike, then moves through "
             "the right sequence of preparation, refinement, and finishing."),
    "note": "Nothing is rushed. From first rinse to final wipe-down, each stage is carried out with patience and intent.",
    "counter": "4 / 4",
    "panels": [
        ("01", "Assessment",
         "We assess condition, surfaces, and the areas that require a gentler or more corrective approach before anything is touched.",
         "assets/img/gallery2.webp"),
        ("02", "Cleanse & Prepare",
         "The bike is washed and prepared properly so that all the work which follows sits on a genuinely clean foundation.",
         "assets/img/gallery6.webp"),
        ("03", "Refine Where Needed",
         "Paint, trim, and metalwork are treated according to condition, for a result that reads noticeably cleaner in person.",
         "assets/img/gallery13.webp"),
        ("04", "Protect & Finish",
         "Protection is applied and a final detailing pass brings everything together with a more composed, presentable finish.",
         "assets/img/gallery17.webp"),
    ],
    "footnote": [("Assess", "condition"), ("Cleanse", "prepare"), ("Refine", "correct"), ("Protect", "finish")],
    "cta": ("Questions about our process? We're here to help.", "#contact"),
}

# ------------------------------------------------------------- 003 EXHAUST
EXHAUST = {
    "label": "Exhaust Revival",
    "index": "003",
    "headline": "Exhausts, brought back to life.",
    "body": ("A closer look at restored metalwork, cleaner surfaces, and the kind of "
             "finish that shows immediately."),
    "sets": [
        ("Set 01", "Exhaust cleaning comparison, before and after refinement.",
         "assets/video/exhaustbefore1.mp4", "assets/video/exhaustafter1.mp4"),
        ("Set 02", "Built-up dullness removed for a noticeably cleaner, brighter finish.",
         "assets/video/exhaustbefore2.mp4", "assets/video/exhaustafter2.mp4"),
        ("Set 03", "Another before-and-after result showing restored metalwork clarity.",
         "assets/video/exhaustbefore3.mp4", "assets/video/exhaustafter3.mp4"),
    ],
    "spec": [("Advanced", "metal refinement"), ("Stainless", "chrome & titanium"),
             ("Oxidation", "and heat staining"), ("Gold Class", "treatment included")],
    "cta": ("Ask about exhaust enhancement", "#contact"),
}

# --------------------------------------------------------------- 004 REELS
REELS = {
    "label": "Behind The Work",
    "index": "004",
    "headline": "A closer look at our work in motion.",
    "body": "A moving showcase of the process, the pace, and the hands behind the finish.",
    "clips": ["assets/video/reel1.mp4", "assets/video/reel2.mp4", "assets/video/reel3.mp4",
              "assets/video/reel4.mp4", "assets/video/reel5.mp4", "assets/video/reel6.mp4"],
    "cta": ("Follow the work on Instagram", "https://www.instagram.com/motosakadetailing"),
}

# ------------------------------------------------------------ 005 PACKAGES
PACKAGES = {
    "label": "Packages",
    "index": "005",
    "headline": "A considered range of treatments.",
    "body": ("A considered range of treatments for cleaner finishes, sharper presentation, "
             "and better-kept rides."),
    "note": "Pricing is per session. Correction and restoration work is quoted after assessment.",
    "plans": [
        {"kicker": "Regular upkeep", "name": "Premium Plus+", "price": "RM50", "prefix": "",
         "blurb": "Essential upkeep with a cleaner, more polished finish.",
         "duration": "45 min – 1 hour", "img": "assets/img/svc-premiumplus.webp",
         "features": ["pH-neutral wash with snow foam", "Wheels, chain and key areas carefully cleaned",
                      "Hand-dried with ceramic wax finish", "Leather conditioning and engine dressing"],
         "cta": "Reserve Premium Plus+", "featured": False},
        {"kicker": "Most requested", "name": "Signature Treatment", "price": "RM80", "prefix": "",
         "blurb": "A more complete treatment with added depth, refinement, and protection.",
         "duration": "1 – 1 hour 45 min", "img": "assets/img/svc-signaturestandard.webp",
         "features": ["Builds on the Premium Plus+ foundation", "Exterior sealant and focused grooming work",
                      "Leather restoration option, where suitable", "Cleansing paste and final presentation finish"],
         "cta": "Reserve Signature Treatment", "featured": True},
        {"kicker": "Gloss-focused finish", "name": "Gold Class Detail", "price": "RM150", "prefix": "",
         "blurb": "For riders who prefer a richer gloss and a more dressed finish.",
         "duration": "1 – 2 hours", "img": "assets/img/svc-goldclass.webp",
         "features": ["Builds on Premium Plus+ and Signature Treatment", "Gold Class wash shampoo & conditioner",
                      "Deeper wheel cleansing", "Gold Class Carnauba wax finish"],
         "cta": "Reserve Gold Class Detail", "featured": False},
        {"kicker": "Corrective refinement", "name": "Level 3 Correction Detail", "price": "RM350", "prefix": "From",
         "blurb": "For paintwork that calls for serious refinement and restored clarity.",
         "duration": "4 – 5 hours", "img": "assets/img/svc-level3correction.webp",
         "features": ["Three-stage paint correction", "Engine bay detailing",
                      "Targets swirls, marks and light scratching", "Approx. 80% to 95% correction"],
         "cta": "Request Consultation", "featured": False},
        {"kicker": "Metal refinement", "name": "Signature Exhaust Enhancement", "price": "RM550", "prefix": "From",
         "blurb": "A focused treatment to restore depth and lustre to tired metalwork.",
         "duration": "4 – 5 hours", "img": "assets/img/svc-signatureexhaust.webp",
         "features": ["Advanced metal refinement", "Suitable for stainless steel, chrome or titanium",
                      "Addresses oxidation and heat staining", "Includes Gold Class Treatment"],
         "cta": "Request Consultation", "featured": False},
        {"kicker": "Extensive restoration", "name": "Bespoke Full Restoration", "price": "RM1200", "prefix": "From",
         "blurb": "An extensive restoration service for neglected machines and special projects.",
         "duration": "1 – 2 days", "img": "assets/img/svc-bespokefull.webp",
         "features": ["Deep cleansing of difficult-to-reach areas", "Careful removal of selected panels and covers",
                      "Paint correction and ceramic protection", "Includes Gold Class Treatment"],
         "cta": "Request Consultation", "featured": False},
    ],
    "cta": ("Not sure which package fits? Ask us.", "#contact"),
}

# ----------------------------------------------------------------- 006 FAQ
FAQ = {
    "label": "Questions & Answers",
    "index": "006",
    "headline": "A few details riders usually ask about.",
    "body": "Simple answers to the things riders check before booking their first appointment.",
    "items": [
        ("Which package suits my bike best?",
         "For regular upkeep, Premium Plus+ is a strong place to start. For a more complete finish with added "
         "refinement and protection, Signature Treatment is usually the preferred option."),
        ("How long does each service usually take?",
         "Timing depends on the level of work. Maintenance packages are usually completed within one to two hours, "
         "while correction or restoration work may require several hours or up to two days."),
        ("Do I need to book first?",
         "Yes. All work is appointment-based so each motorcycle can be given the proper time and attention."),
        ("Do you work on used bikes and paint correction?",
         "Yes. Pre-owned bikes, neglected finishes, and paint correction requests can be assessed privately based "
         "on condition and the result you want."),
        ("Is ceramic protection included in every package?",
         "Not in every package. Ceramic protection is usually recommended where the level of correction or "
         "restoration calls for it."),
        ("What makes Signature Treatment different?",
         "It moves beyond routine upkeep with a more complete combination of finish work, protection, grooming, "
         "and presentation detailing."),
        ("How does the loyalty card work?",
         "Each return visit earns a stamp, with rewards unlocked over time. Final reward tiers can be tailored as "
         "the programme develops."),
        ("How do I book through WhatsApp?",
         "Simply tap any booking button on the site. A prefilled message will open so your enquiry can be sent in seconds."),
    ],
    "aside": {
        "title": "Still have a question?",
        "body": ("Every bike arrives in a different condition. Send a photo and a short note, and we will tell you "
                 "honestly what it needs — and what it does not."),
        "cta": "Let's have a chat",
    },
    "marquee": "refined care for bikes of distinction —",
}

# ---------------------------------------------------------------- 007 TEAM
# PLACEHOLDER CONTENT — awaiting real team details and photographs from Motosaka.
TEAM = {
    "label": "Meet the Team",
    "index": "007",
    "headline": "Get to know the hands behind the finish.",
    "body": "Makers, thinkers, and problem-solvers who care about how a bike leaves the unit.",
    "placeholder_note": "Placeholder — team details and photographs to be supplied.",
    "members": [
        ("Lorem Ipsum", "Dolor Sit Amet",
         "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et "
         "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip "
         "ex ea commodo consequat.", "assets/img/team1.webp"),
        ("Consectetur Adipiscing", "Elit Sed Do",
         "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
         "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est "
         "laborum sed ut perspiciatis.", "assets/img/team2.webp"),
        ("Eiusmod Tempor", "Incididunt Labore",
         "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam "
         "rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt.",
         "assets/img/team3.webp"),
        ("Magna Aliqua", "Ut Enim Ad",
         "Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni "
         "dolores eos qui ratione voluptatem sequi nesciunt neque porro quisquam est qui dolorem ipsum.",
         "assets/img/team4.webp"),
        ("Minim Veniam", "Quis Nostrud",
         "Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia "
         "non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.",
         "assets/img/team5.webp"),
        ("Exercitation Ullamco", "Laboris Nisi",
         "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid "
         "ex ea commodi consequatur quis autem vel eum iure reprehenderit qui in ea voluptate velit esse.",
         "assets/img/team6.webp"),
    ],
    "cta": ("Say hello on WhatsApp", "#contact"),
}

# ------------------------------------------------------------- 008 REVIEWS
REVIEWS = {
    "label": "Google Reviews",
    "index": "008",
    "headline": "What riders say after picking up their bikes.",
    "body": "Rated 5.0 by riders who value finish, care, and attention to detail.",
    "rating": "5.0",
    "items": [
        ("Mystic Tora", "5 months ago",
         "I sent my bike in for their Level 3 package and honestly, the results blew me away. My bike came back "
         "looking like absolute showroom condition. They dismantled carefully and detailed my exhaust also — it "
         "came out super shiny and cleaner than I've seen it. Throughout the whole process, they gave timely "
         "updates on the progress, which really shows how trustworthy, transparent, and professional they are."),
        ("Xiang Hui", "8 months ago",
         "Hapek did an outstanding job washing my bike! He's incredibly detailed and meticulous, making sure every "
         "corner is spotless. I honestly don't think you can find the same level of service anywhere else at this "
         "price. I especially love how the engine bay shines after the wash — it looks like new!"),
        ("Yves Hakim", "7 months ago",
         "Shoutout to Motosaka for the incredible job on my bike! The detailing was top-notch, every part of the "
         "bike looked spotless, polished, and just overall stunning. It honestly felt like I was picking up a brand "
         "new ride. The person behind Motosaka was incredibly humble and friendly."),
        ("uzair a'lfullah", "6 months ago",
         "Sent my bike for the Level 3 Correction Detail and honestly I'm super happy with the result. My bike looks "
         "so clean and glossy, no swirls or scratches visible anymore. Not a single bit of dust left, feels like I "
         "just got a brand new bike again. Totally worth it and highly recommended!"),
        ("Dominic Lim", "2 months ago",
         "I'll let the photos speak for themselves. Great vibes, wonderful quality. The time and effort took by "
         "Hapek and his partner really shows. Thanks once again."),
        ("Md Shahz", "8 months ago",
         "Affordable and best detailing ever done by a humble and talented guy! He is super friendly, accommodating "
         "and detailed in his work. Highly recommended — he basically transformed our bikes to make them look like "
         "brand new again!"),
        ("Iswandy Isa", "9 months ago",
         "Motosaka is one of the best wash and detailing. Awesome! Never seen or met a superb service like yours. "
         "Definitely coming back. One thing I like about this home-base service — the vibe, chill and relax."),
        ("Ronan Keida", "5 months ago",
         "Brought my bike to Motosaka Detailing, and they did an amazing job! The attention to detail was incredible, "
         "every surface looks spotless and the finish is better than when I first got it. Super professional, "
         "friendly team, and clearly passionate about what they do."),
        ("Noraini Abas", "9 months ago",
         "I recently sent my bike for detailing and I have to say the results exceeded my expectations. The attention "
         "to detail was outstanding and the level of care put into every corner of the bike truly shows his passion "
         "and professionalism. I'll definitely be returning for future treatments."),
    ],
    "cta": ("Read every review on Google", "https://www.google.com/search?q=Motosaka+Detailing+Johor+Bahru"),
}

# ------------------------------------------------------------ 009 AFTERCARE
AFTERCARE = {
    "label": "Aftercare & Loyalty",
    "index": "009",
    "headline": "Looked after, long after the appointment.",
    "body": ("Two quiet extras for riders who keep their motorcycles in consistently good order — "
             "a care kit for the ride after, and a card that rewards the ones who keep coming back."),
    "cards": [
        {"kicker": "Complimentary Aftercare", "title": "Refresh Care Kit",
         "lede": "A thoughtful extra, prepared for the ride after.",
         "body": ("A compact aftercare essential for riders who want their bike to stay cleaner, "
                  "fresher, and better kept between visits."),
         "img": "assets/img/carekit.webp", "fit": "contain",
         "meta": [("Included with", "Gold Class and above"), ("Purpose", "Post-detail refresh & upkeep")],
         "points": ["Helps maintain a cleaner, fresher feel after regular rides",
                    "Designed to extend the cared-for finish between visits",
                    "Compact, useful, and aligned with the Motosaka standard of care"]},
        {"kicker": "Loyalty", "title": "The Loyalty Card",
         "lede": "Reserved for returning riders.",
         "body": ("For those who keep their motorcycles in consistently good order, the loyalty card "
                  "offers a quieter way to reward repeat visits."),
         "img": "assets/img/loyalty-back.webp", "fit": "contain",
         "meta": [("Earn", "One stamp per visit"), ("Unlock", "Free Premium & Signature wash")],
         "points": ["Each return visit earns a stamp on the card",
                    "Rewards unlock over time as the card fills",
                    "Reward tiers can be tailored as the programme develops"]},
    ],
    "cta": ("Ask about Gold Class", "#contact"),
}


CONTACT = {
    "label": "Contact",
    "kicker": "Got a bike, a question, or a project?",
    "headline": "Let's talk.",
    "body": ("Every bike arrives in a different condition. Send a photo and a short note and we'll come back to "
             "you with what it needs — and what it doesn't."),
    "offer_title": "What we offer",
    "offers": ["Appointment-only detailing", "Paint correction and restoration",
               "Exhaust and metalwork refinement", "Aftercare and loyalty rewards"],
    "form_fields": [("name", "text", "Your Name", True), ("email", "email", "Your Email", True),
                    ("bike", "text", "Your Bike (make & model)", False)],
    "form_message": "Tell us about the bike and what you'd like done",
    "package_label": "Which treatment are you after?",
    "package_default": "Not sure yet — please advise",
    "submit": "Send enquiry",
    "legal": "By submitting, you agree to be contacted about your enquiry.",
    "socials": [("Instagram", "https://www.instagram.com/motosakadetailing"),
                ("WhatsApp", "https://wa.me/60124058765"),
                ("Email", "mailto:motosakadetailing@gmail.com")],
}

FOOTER = {
    "blurb": ("Refined detailing, correction, and restoration for motorcycles that deserve a more "
              "considered finish."),
    "cols": [
        ("Explore", [("Work", "#work"), ("Process", "#process"), ("Packages", "#packages"),
                     ("Reviews", "#reviews"), ("FAQ", "#faq")]),
        ("Studio", [("Aftercare", "#aftercare"), ("The Team", "#team"), ("Contact", "#contact"),
                    ("WhatsApp", "https://wa.me/60124058765"),
                    ("Instagram", "https://www.instagram.com/motosakadetailing")]),
    ],
    "newsletter_title": "Keep up with the work",
    "newsletter_body": "Occasional notes on new treatments, availability, and finished builds.",
    "copyright": "© 2026 Motosaka Detailing. All rights reserved.",
}
