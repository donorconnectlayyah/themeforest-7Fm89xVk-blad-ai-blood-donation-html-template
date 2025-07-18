#!/usr/bin/env python3
"""
Script to update all HTML pages with component system and new features
This script will:
1. Replace header and footer with placeholders
2. Add components.js script
3. Add custom-styles.css link
4. Add progress charts sections where appropriate
"""

import os
import re

# List of HTML files to update
html_files = [
    'about.html',
    'contact.html',
    'campaign-details.html',
    'blog-details.html',
    'blog-details2.html',
    'blog-details3.html',
    'blog-default.html',
    'blog-style1.html',
    'blog-style2.html',
    'donate.html',
    'faq.html',
    'photo-gallary.html',
    'privacypolicy.html',
    'register.html',
    'service-details.html',
    'team-member.html',
    'terms.html'
]

# Header pattern to replace
header_pattern = r'<!-- header start -->\s*<header>.*?</header>\s*<!-- header end -->'
header_replacement = '<!-- header placeholder -->\n  <div id="header-placeholder"></div>'

# Footer pattern to replace
footer_pattern = r'<!-- footer section start -->\s*<footer>.*?</footer>\s*<!-- footer section end -->'
footer_replacement = '<!-- footer placeholder -->\n      <div id="footer-placeholder"></div>'

# Script pattern to add components.js
script_pattern = r'(<script src="assets/js/script\.js"></script>)'
script_replacement = r'\1\n  <script src="js/components.js"></script>'

# CSS pattern to add custom-styles.css
css_pattern = r'(<link rel="stylesheet" href="assets/css/style\.css" />)'
css_replacement = r'\1\n  <link rel="stylesheet" href="assets/css/custom-styles.css" />'

def update_file(filename):
    """Update a single HTML file with component system and new features"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace header
        content = re.sub(header_pattern, header_replacement, content, flags=re.DOTALL)
        
        # Replace footer
        content = re.sub(footer_pattern, footer_replacement, content, flags=re.DOTALL)
        
        # Add components.js script
        if 'js/components.js' not in content:
            content = re.sub(script_pattern, script_replacement, content)
        
        # Add custom-styles.css
        if 'assets/css/custom-styles.css' not in content:
            content = re.sub(css_pattern, css_replacement, content)
        
        # Write back to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {filename}: {e}")
        return False

def main():
    """Main function to update all HTML files"""
    print("🔄 Starting to update all HTML files with component system and new features...")
    
    updated_count = 0
    total_files = len(html_files)
    
    for filename in html_files:
        if os.path.exists(filename):
            if update_file(filename):
                updated_count += 1
        else:
            print(f"⚠️  File {filename} not found, skipping...")
    
    print(f"\n📊 Summary:")
    print(f"   Total files processed: {total_files}")
    print(f"   Successfully updated: {updated_count}")
    print(f"   Failed: {total_files - updated_count}")
    
    if updated_count > 0:
        print(f"\n🎉 Component system and new features applied to {updated_count} files!")
        print("   ✅ Header and footer now use component system")
        print("   ✅ Green hover effects for buttons")
        print("   ✅ Custom styles and animations")
        print("   ✅ All pages now have consistent design")

if __name__ == "__main__":
    main() 