# Influencer Recruitment Web App

A Django-based web application designed to connect brands with influencers. Brands can create campaigns, review influencer applications, and manage collaborations. Influencers can create profiles, explore active campaigns, and apply to those that fit their niche.

## Features

### For Influencers
- User registration and authentication
- Profile creation with bio, social media links, and follower stats
- Browse and search for brand campaigns
- Apply to campaigns with custom proposals
- Track application status

### For Brands
- Brand signup and login
- Create and manage recruitment campaigns
- Filter and review influencer applications
- View influencer profiles and contact them
- Dashboard for campaign stats

### Admin Panel
- Manage users (brands and influencers)
- Approve or reject campaigns and applications
- Content moderation

---

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, CSS, Bootstrap (or your preferred CSS framework)
- **Database:** SQLite (development), PostgreSQL (production recommended)
- **Authentication:** Django built-in auth (JWT optional for API access)
- **Hosting:** Compatible with Heroku, DigitalOcean, Namecheap VPS, etc.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/influencer-recruitment.git
   cd influencer-recruitment
