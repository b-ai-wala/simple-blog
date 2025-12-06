#!/usr/bin/env python3
import os
import re
import glob

posts_dir = "/Users/burhan/github-burhan-ai-wala-vscode/research/simple-blog/posts"
md_files = glob.glob(f"{posts_dir}/*.md")

# Manual mapping of incorrect references to actual filenames
filename_fixes = {
    '3-attribution-models-1.png': '3-attribution-models.png',
    'CAC-By-Channel-1st-Click-Attribution-2.png': 'CAC-By-Channel---1st-Click-Attribution-(1).png',
    'CAC-By-Channel-Last-Click-Attribution-2.png': 'CAC-By-Channel---Last-Click-Attribution-(2).png',
    'Screenshot-2022-08-07-at-1.24.55-AM.png': 'Screenshot-2022-08-07-at-1.24.55-AM.png',
    'Screenshot-2022-08-07-at-1.25.03-AM.png': 'Screenshot-2022-08-07-at-1.25.03-AM.png',
    'Screenshot-2022-08-07-at-12.37.55-AM-1.png': 'Screenshot-2022-08-07-at-12.37.55-AM-1.png',
    'Screenshot-2022-08-27-at-1.44.30-AM.png': 'Screenshot-2022-08-27-at-1.44.30-AM.png',
    'Screenshot-2022-09-23-at-1.09.33-AM.png': 'Screenshot-2022-09-23-at-1.09.33-AM.png',
    'Screenshot-2022-09-23-at-1.12.53-AM.png': 'Screenshot-2022-09-23-at-1.12.53-AM.png',
    'Screenshot-2022-09-23-at-1.18.47-AM.png': 'Screenshot-2022-09-23-at-1.18.47-AM.png',
    'Screenshot-2022-09-23-at-1.27.56-AM.png': 'Screenshot-2022-09-23-at-1.27.56-AM.png',
    'Total-Transactions-1.png': 'Total-Transactions-1.png',
    'Users-over-time-1.png': 'Users-over-time.png',
    'OYO-Loop-B-1.png': 'OYO-Loop-B.png',
    'Atomic-Unit-1.png': 'Atomic-Unit.png',
}

total_fixes = 0
files_updated = 0

for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace known bad references
    for bad_name, good_name in filename_fixes.items():
        if bad_name in content:
            content = content.replace(f'/images/{bad_name}', f'/images/{good_name}')
            total_fixes += 1

    if content != original_content:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        files_updated += 1
        print(f"Updated: {os.path.basename(md_file)}")

print(f"\nTotal: {total_fixes} image references fixed in {files_updated} files")
