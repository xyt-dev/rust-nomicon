#!/usr/bin/env python3
import re
import sys
import subprocess

def convert_to_wizard(text):
    """使用 wtg 命令转换文本"""
    if not text.strip():
        return text
    try:
        result = subprocess.run(['wtg'], input=text, text=True, capture_output=True)
        return result.stdout.rstrip('\n')
    except:
        return text

def convert_text_preserve_code_markers(text):
    """转换文本，包括代码内容，但保护反引号标记"""
    # 找到所有行内代码，转换内容但保留反引号
    def convert_code(m):
        code_content = m.group(1)
        converted_content = convert_to_wizard(code_content)
        return f"`{converted_content}`"
    
    text = re.sub(r'`([^`]+)`', convert_code, text)
    
    # 转换剩余文本
    # 保护已经处理过的代码块
    codes = []
    def save_code(m):
        codes.append(m.group(0))
        return f"___55{len(codes)-1}55___"
    text = re.sub(r'`[^`]+`', save_code, text)
    
    text = convert_to_wizard(text)
    
    # 恢复代码块
    for i, code in enumerate(codes):
        text = text.replace(f"___55{i}55___", code)
    
    return text

def process_line(line):
    """处理单行，保护链接和代码"""
    # 引用链接定义 - 转换标识符但保持 URL
    m = re.match(r'^(\[.+\]):\s+(.+)$', line)
    if m:
        ref_id = m.group(1)
        url = m.group(2)
        # 转换引用标识符（包括其中的代码）
        converted_id = convert_text_preserve_code_markers(ref_id)
        return f"{converted_id}: {url}"
    
    # HTML 标签行不转换（仅完整的标签行）
    if re.match(r'^<[^>]+>$', line.strip()):
        return line
    
    # 空行不转换
    if not line.strip():
        return line
    
    # 保存所有需要保护的部分
    protected = []
    
    # 只保护真正的 HTML 标签（包含属性的，如 <div class="...">）
    # 不保护泛型如 <T>
    def protect_html(m):
        tag = m.group(0)
        # 只保护包含空格、等号、斜杠的标签（真正的HTML）
        # 或者常见的HTML标签名
        if ' ' in tag or '=' in tag or tag.startswith('</') or re.match(r'<(div|span|p|a|ul|ol|li|table|tr|td|br|hr|img|script|style|meta|link|head|body|html)', tag, re.I):
            protected.append(tag)
            return f"___77{len(protected)-1}77___"
        return tag  # 不保护泛型如 <T>
    line = re.sub(r'<[^>]+>', protect_html, line)
    
    # 保护引用链接 [text][ref] - 转换 text（包括代码内容）和 ref
    def protect_ref_link(m):
        text = m.group(1)
        ref = m.group(2)
        # 转换文本和引用标识
        conv_text = convert_text_preserve_code_markers(text)
        conv_ref = convert_text_preserve_code_markers(ref)
        protected.append(f"[{conv_text}][{conv_ref}]")
        return f"___66{len(protected)-1}66___"
    line = re.sub(r'\[([^\]]+)\]\[([^\]]+)\]', protect_ref_link, line)
    
    # 保护普通链接 [text](url) - 转换 text（包括代码内容）但保护 url
    def protect_link(m):
        text = m.group(1)
        url = m.group(2)
        # 转换文本，包括代码内容
        conv_text = convert_text_preserve_code_markers(text)
        protected.append(f"[{conv_text}]({url})")
        return f"___99{len(protected)-1}99___"
    line = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', protect_link, line)
    
    # 处理行内代码 - 转换内容但保留反引号
    def convert_inline_code(m):
        code_content = m.group(1)
        converted = convert_to_wizard(code_content)
        protected.append(f"`{converted}`")
        return f"___88{len(protected)-1}88___"
    line = re.sub(r'`([^`]+)`', convert_inline_code, line)
    
    # 转换剩余文本
    line = convert_to_wizard(line)
    
    # 恢复所有保护的内容
    for i, item in enumerate(protected):
        line = line.replace(f"___88{i}88___", item)
        line = line.replace(f"___77{i}77___", item)
        line = line.replace(f"___66{i}66___", item)
        line = line.replace(f"___99{i}99___", item)
    
    return line

def process_markdown(content):
    """处理整个 markdown 文件"""
    lines = content.split('\n')
    result = []
    in_code_block = False
    
    for line in lines:
        # 代码块标记
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue
        
        # 代码块内不转换
        if in_code_block:
            result.append(line)
            continue
        
        # 处理普通行
        result.append(process_line(line))
    
    return '\n'.join(result)

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    processed = process_markdown(content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(processed)
