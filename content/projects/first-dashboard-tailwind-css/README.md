# A simple Dashboard with Tailwind CSS

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/first-dashboard-tailwind-css/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

🌐 _Estas instrucciones también están [disponibles en español](./README.es.md)_.

**Before you start**:

> We need you! These exercises are built and maintained in collaboration with people like you. If you find any bugs 🐞 or typos, please contribute and/or report them.

<!-- endhide -->

---

## 🎯 Your challenge

An influencer is starting to work with brands and contacts you because she needs to measure the impact of their ads and conversion. The problem is that they have multiple social media accounts (Instagram, TikTok, YouTube, etc.) and need to understand how to consolidate all this information in a reporting dashboard to answer basic questions such as:

- How much money am I generating in commissions?
- Which products are generating the most revenue?
- How well are my ads converting (conversions / reach)?
- Which platforms are generating the best return (revenue/costs)?
- What is the _engagement rate_ by platform and by product?

The influencer contacts you because they need a clear report (a dashboard) that allows them to oversee their business without getting lost in data scattered across multiple platforms. And you, although you are just getting started, want to deliver a solid, professional proposal—so your mission is to design a dashboard that consolidates information from all their social media accounts and shows them what matters most for making quick decisions.

**Business context:**

- They have 3 products they promote with three different prices (Product A: €50, Product B: €120, Product C: €80)
- For each sale generated, they receive a 15% commission

---

### What makes a dashboard "good"?

Organize the dashboard into broad blocks:

**1️⃣ Top block:** Main outcome indicators (KPI):

- **Volume:** sales, sign-ups, active users, impressions
- **Revenue:** revenue (commissions, sales), MRR (monthly recurring revenue in subscriptions), average selling price
- **Engagement:** _engagement_ rate, total interactions, conversion rate
- **Retention:** churn (churn rate), persistence, completion rate of the sales or subscription process
- **Performance:** total conversions, click-through rate (CTR), conversion rate
- **Satisfaction:** loyalty score (NPS), satisfaction score (CSAT)
- **Efficiency:** cost per outcome, margin, lead times

**2️⃣ Middle block:** "Drivers" (factors that explain the outcome):

- **Conversion** by stage (sales funnel)
- **Performance by platform** (Instagram, TikTok, YouTube, etc.)
- **Quality** (qualified lead ratio, _attendance rate_, _pass rate_)
- **Performance by product** (which product generates more commissions and better conversion)
- **Activity** (posts published, stories, reels, videos by platform)
- **Engagement** (likes, comments, shares, saves by platform)

**3️⃣ Bottom block:** Operational details (tables/lists, alerts):

- Products table: price, commissions generated, conversions, ROI per product
- Platforms table: reach, engagement, conversions, best platform by metric
- Campaigns table: dates, products promoted, results, performance
- Alerts: sharp drops in conversion, conversion spikes, performance anomalies
- Lists with filters: "top products", "top platforms", "top campaigns", "improvement opportunities"

> Example of an administrative dashboard:

![Dashboard example](images/image1.png "Dashboard example")

---

## 🌱 How to start the project

Open the template repository using a provisioning tool such as [Codespaces](https://4geeks.com/lesson/what-is-github-codespaces) (recommended) or clone it locally:

```text
https://github.com/4GeeksAcademy/html-hello
```

Follow the steps in [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project).

💡 **Important:** Create a new repository on GitHub for your code, update the remote (`git remote set-url origin <your-new-url>`) and push your changes with `add`, `commit` and `push`.

---

## 💻 What you need to do

Build a dashboard that shows at least **three KPIs**, **three drivers**, and **operational details** (tables or lists) in the three blocks described above. It must work well on **mobile, tablet, and desktop** (at least three breakpoints; design **mobile-first**).

- [ ] **Plan the layout:** Decide the main structure: navbar/header or sidebar, and how the content is split (top block = KPIs, middle = drivers, bottom = tables/lists). Think in **reusable components** (cards, widget boxes, tables) and section-based structure.
- [ ] **Design mobile-first:** Start from the smallest screen; then adapt with Tailwind breakpoints (`sm:`, `md:`, `lg:`) so the same components work on tablet and desktop. Avoid pixel-based sizes; use Tailwind spacing and sizing utilities.
- [ ] **Use semantic HTML:** Use appropriate tags (`<header>`, `<nav>`, `<main>`, `<section>`, `<table>`, etc.) so the dashboard has a clear document outline.
- [ ] **Use Tailwind only:** Apply styles with Tailwind utility classes (and Preflight if you use the Tailwind build). Do not mix in other CSS frameworks or custom CSS except for Chart CSS if needed.
- [ ] **Charts (optional):** For KPIs or drivers you can use [Chart CSS](https://chartscss.org/) (CSS-only). Data can be sample data; focus on clear hierarchy and readability.
- [ ] **Consistency:** Reuse the same patterns for similar elements (e.g. all KPI cards share the same structure and style).

⚠️ **IMPORTANT:** This project uses **only HTML and Tailwind CSS**. Tell your AI Copilot **not to use other technologies** (e.g. React, Vue). Say this at the start.

---

## ✅ What we will evaluate

- [ ] **Semantic HTML:** Correct use of structural and landmark tags; clear, logical hierarchy.
- [ ] **Tailwind CSS:** Styles applied via utility classes; no conflicting or redundant custom CSS; appropriate use of breakpoints and layout utilities (flex/grid).
- [ ] **Layout and components:** Clear separation of the three blocks (KPIs, drivers, operational); consistent grouping and visual hierarchy; reusable-looking components (cards, sections, tables).
- [ ] **Responsive design:** Usable on at least three device sizes (e.g. phone, tablet, desktop); mobile-first approach; no horizontal scroll or broken layout on small screens.

> Note: We do not grade whether the chosen KPIs or drivers are “correct” for the business; we evaluate structure, Tailwind usage, and responsiveness.

---

## 📦 How to submit this project

You must submit a repository that includes the HTML document with the full structure and the CSS with the styles and media queries needed to adapt the dashboard to the different _breakpoints_.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. Find out more about the [AI Engineering](https://4geeksacademy.com/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/coding-bootcamps/cybersecurity), and [Full-Stack Software Developer](https://4geeksacademy.com/coding-bootcamps/full-stack-developer) [courses](https://4geeksacademy.com/en/program-comparison).
