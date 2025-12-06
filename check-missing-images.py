#!/usr/bin/env python3
import os
import re
import glob

posts_dir = "/Users/burhan/github-burhan-ai-wala-vscode/research/simple-blog/posts"
images_dir = "/Users/burhan/github-burhan-ai-wala-vscode/research/simple-blog/public/images"
md_files = glob.glob(f"{posts_dir}/*.md")

# Get all referenced images
referenced_images = set()
for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all image references
    matches = re.findall(r'/images/([^\)]+)', content)
    referenced_images.update(matches)

# Get all actual image files
actual_images = set(os.listdir(images_dir))

# Find missing images
missing = []
for img in referenced_images:
    if img not in actual_images:
        # Check if it exists with different extension or name
        base_name = os.path.splitext(img)[0]
        found = False
        for actual in actual_images:
            if base_name in actual:
                print(f"MISMATCH: {img} -> maybe {actual}")
                found = True
                break
        if not found:
            missing.append(img)

if missing:
    print(f"\nMISSING {len(missing)} images:")
    for img in sorted(missing):
        print(f"  - {img}")
else:
    print("All referenced images exist!")
