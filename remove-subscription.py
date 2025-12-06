#!/usr/bin/env python3
import os
import re
import glob

posts_dir = "/Users/burhan/github-burhan-ai-wala-vscode/research/simple-blog/posts"
md_files = glob.glob(f"{posts_dir}/*.md")

# Pattern to match the subscription section
subscription_pattern = r'Email\(required\)\s*Subscribe here for an occasional email.*?Subscribe to Growth Notes by Burhan'

files_updated = 0

for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Remove the subscription section
    content = re.sub(subscription_pattern, '', content, flags=re.DOTALL)

    if content != original_content:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        files_updated += 1
        print(f"Updated: {os.path.basename(md_file)}")

print(f"\nTotal: {files_updated} posts updated - removed subscription section")
