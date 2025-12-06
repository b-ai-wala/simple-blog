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

    # Pattern to match image references with /images/ path
    pattern = r'!\[([^\]]*)\]\(/images/([^)]+)\)'

    def fix_spaces(match):
        global total_fixes
        alt_text = match.group(1)
        filename = match.group(2)

        # Replace spaces with dashes in filename
        if ' ' in filename:
            total_fixes += 1
            new_filename = filename.replace(' ', '-')
            return f'![{alt_text}](/images/{new_filename})'
        return match.group(0)

    content = re.sub(pattern, fix_spaces, content)

    if content != original_content:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        files_updated += 1
        print(f"Updated: {os.path.basename(md_file)}")

print(f"\nTotal: {total_fixes} image paths fixed in {files_updated} files")
