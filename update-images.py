#!/usr/bin/env python3
import os
import re
import glob

# Directory containing markdown posts
posts_dir = "/Users/burhan/github-burhan-ai-wala-vscode/research/simple-blog/posts"

# Get all markdown files
md_files = glob.glob(f"{posts_dir}/*.md")

# Mapping of common filename variations
filename_mapping = {
    'Marketing-Budget-Revised-4.png': 'Marketing Budget Revised.png',
    'Acquisition-Budget-graphic-1.png': 'Acquisition Budget graphic.png',
    'A-new.png': 'A new.png',
    'B-New.png': 'B New.png',
    'Graph-of-First-time-users.png': 'Graph of First time users.png',
    'Graph-of-Win-Time.png': 'Graph of Win Time.png',
    'Graph-of-Winners.png': 'Graph of Winners.png',
    'Group-10.png': 'Group 10.png',
    'Group-22.png': 'Group 22.png',
    'Growth-Blindspot-Logo-1.png': 'Growth Blindspot Logo.png',
    'Customer-Single-View.png': 'Customer Single View.png',
    'Product-Usage-Data.png': 'Product Usage Data.png',
    'Team-wise-Data-Silo.png': 'Team wise Data Silo.png',
    'Transaction-Data.png': 'Transaction Data.png',
    'CRM-Engagement.png': 'CRM Engagement.png',
    'Acquisition-Data.png': 'Acquisition Data.png',
    'Scale-vs-CAC.png': 'Scale vs CAC.png',
    'Channels-Comparison-1.png': 'Channels Comparison 1.png',
    'Channels-Comparison-2.png': 'Channels Comparison 2.png',
    'Discount-Group.png': 'Discount Group.png',
    'Discount-vs-Transactions.png': 'Discount vs Transactions.png',
    'Discount-vs-ROI-v2.png': 'Discount vs ROI v2.png',
    'Discount-vs-ROI-v3.png': 'Discount vs ROI v3.png',
    'Atomic-Unit-1.png': 'Atomic Unit.png',
    'ROI-Equation.png': 'ROI Equation.png',
    'Time-Delay-Acquisition-with-Channel-Mix.png': 'Time Delay Acquisition with Channel Mix.png',
    'Time-Delay-Acquisition.png': 'Time Delay Acquisition.png',
    'Total-Transactions-1.png': 'Total Transactions.png',
    'Blake-Meme.png': 'Blake Meme.png',
    'Impressions-vs-Reach.png': 'Impressions vs Reach.png',
    'time-to-convert.png': 'time to convert.png',
    'Stages-1.png': 'Stages.png',
    'kermit-worried.gif': 'kermit-worried.gif',
}

total_replacements = 0
files_updated = 0

for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Find all Wayback Machine image URLs
    wayback_pattern = r'https://web\.archive\.org/web/\d+im_/https://[^)]+?\.(png|jpeg|jpg|gif|svg)'

    def replace_url(match):
        global total_replacements
        url = match.group(0)

        # Extract just the filename from the URL
        # Handle URLs with query parameters
        filename = url.split('/')[-1].split('?')[0]

        # Check if we have a mapped filename
        if filename in filename_mapping:
            local_filename = filename_mapping[filename]
        else:
            # Try to find the file with spaces instead of dashes
            local_filename = filename.replace('-', ' ')
            if not os.path.exists(f'/Users/burhan/github-burhan-ai-wala-vscode/research/simple-blog/public/images/{local_filename}'):
                local_filename = filename

        total_replacements += 1
        return f'/images/{local_filename}'

    content = re.sub(wayback_pattern, replace_url, content)

    # Also replace any remaining gravatar URLs
    content = re.sub(
        r'https://web\.archive\.org/web/\d+im_/https://secure\.gravatar\.com/[^\)]+',
        '/images/Burhan Photo Main-compressed.jpg',
        content
    )

    if content != original_content:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        files_updated += 1
        print(f"Updated: {os.path.basename(md_file)}")

print(f"\nTotal: {total_replacements} image URLs replaced in {files_updated} files")
