#!/usr/bin/env python3
import os
import re
import glob

posts_dir = "/Users/burhan/github-burhan-ai-wala-vscode/research/simple-blog/posts"
md_files = glob.glob(f"{posts_dir}/*.md")

total_fixes = 0
files_updated = 0

for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Pattern to match duplicate images: ![...](...) immediately followed by ![...](...)
    # This pattern captures the image markdown and checks if it's duplicated
    pattern = r'(!\[[^\]]*\]\([^\)]+\))\1'

    # Count how many will be replaced
    matches = re.findall(pattern, content)
    total_fixes += len(matches)

    # Replace duplicates with single instance
    content = re.sub(pattern, r'\1', content)

    if content != original_content:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        files_updated += 1
        print(f"Updated: {os.path.basename(md_file)} - fixed {len(matches)} duplicates")

print(f"\nTotal: {total_fixes} duplicate images removed from {files_updated} files")
