#!/usr/bin/env python3
import os
import re
import glob

posts_dir = "/Users/burhan/github-burhan-ai-wala-vscode/research/simple-blog/posts"
md_files = glob.glob(f"{posts_dir}/*.md")

# Map old URLs to new slugs
url_to_slug_mapping = {
    '3-reasons-why-referral-marketing-is-not-working-for-your-product-startup': '3-reasons-why-referral-marketing-is-not-working',
    'the-4-types-of-marketing-budgets-1-4-acquisition-budget': '4-types-of-marketing-budgets-1-acquisition',
    'the-4-types-of-marketing-budgets-2-4-discounting-budget': '4-types-of-marketing-budgets-2-discounting',
    'the-4-types-of-marketing-budgets-4-4-brand-marketing-budget': '4-types-of-marketing-budgets-4-brand-marketing',
    'attribution-eats-marketing-strategy-for-breakfast': 'attribution-eats-marketing-strategy-for-breakfast',
    'can-you-grow-your-startup-100x-by-paid-marketing': 'can-you-grow-your-startup-100x-by-paid-marketing',
    'growth-marketing-blind-spot-why-do-we-need-a-customer-single-view': 'growth-marketing-blind-spot-customer-single-view',
    'customer-single-view': 'growth-marketing-blind-spot-customer-single-view',
    'how-do-zomato-oyo-uber-amazon-growth-teams-drive-repeat-usage-of-their-apps': 'how-growth-teams-drive-repeat-usage',
    'what-every-ceo-wants-to-ask-their-marketing-teams-but-seldom-gets-an-answer-to-1-n': 'what-every-ceo-wants-to-ask-marketing-teams',
}

total_replacements = 0
files_updated = 0

for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Pattern to match Wayback Machine URLs
    wayback_pattern = r'https://web\.archive\.org/web/\d+/https?://([^\)]+)'

    def replace_wayback_url(match):
        global total_replacements
        full_url = match.group(1)

        # Check if it's an internal bpitha.com link
        if 'bpitha.com/' in full_url:
            # Extract the slug from the URL
            slug_match = re.search(r'bpitha\.com/([^/\)]+)/?', full_url)
            if slug_match:
                old_slug = slug_match.group(1)

                # Map to new slug if exists
                new_slug = url_to_slug_mapping.get(old_slug, old_slug)

                total_replacements += 1
                return f'/posts/{new_slug}'

        # For external URLs, just return the direct URL
        total_replacements += 1
        return f'https://{full_url}'

    # Replace all Wayback Machine URLs
    content = re.sub(wayback_pattern, replace_wayback_url, content)

    if content != original_content:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        files_updated += 1
        print(f"Updated: {os.path.basename(md_file)}")

print(f"\nTotal: {total_replacements} URLs fixed in {files_updated} files")
