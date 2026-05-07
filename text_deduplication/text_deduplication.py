def process_first_txt(file_path):
    """处理第一个txt：按/* */注释规则提取内容到列表"""
    result_list = []
    in_comment_block = False  # 是否处于/* */注释块内
    comment_buffer = []  # 缓存注释块中间内容
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # 规则1：已在注释块中
            if in_comment_block:
                # 判断当前行是否以 */ 结尾（含换行）
                if line.rstrip('\n').endswith('*/'):
                    # 取 */ 之前的内容存入缓存
                    idx = line.find('*/')
                    comment_buffer.append(line[:idx])
                    # 拼接注释块所有内容，加入列表
                    full_comment = ''.join(comment_buffer)
                    result_list.append(full_comment)
                    # 重置状态
                    in_comment_block = False
                    comment_buffer.clear()
                else:
                    # 注释块中间行，直接缓存
                    comment_buffer.append(line)
                continue
            # 规则2：行以 */ 开头，直接跳过
            if line.strip().startswith('*/') or line.strip().startswith('}'):
                continue
            # 规则3：行以 /* 开头，进入注释块模式
            if line.lstrip().startswith('/*'):
                in_comment_block = True
                # 取 /* 之后的内容存入缓存
                idx = line.find('/*') + 2
                comment_buffer.append(line[idx:])
                continue
            # 规则4：其他普通行，去掉末尾换行符加入列表
            normal_line = line.rstrip('\n')
            result_list.append(normal_line)
    return result_list
def read_second_txt_to_str(file_path):
    """读取第二个txt，整合成一个字符串S"""
    with open(file_path, 'r', encoding='utf-8') as f:
        s = f.read()
    return s
def remove_all_substr(origin_str, substr_list):
    """遍历列表，删除S中所有匹配的完全相同子串"""
    new_str = origin_str
    for sub in substr_list:
        # 循环删除直到不存在该子串
        while sub in new_str:
            new_str = new_str.replace(sub, '')
    return new_str
def save_str_to_txt(content, save_path):
    """保存处理后的字符串到新txt文件"""
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(content)
def do_work(file_dir_list):
    # ========== 请在这里修改你的文件路径 ==========
    first_file = r"新建文本文档.txt"  # 待规则解析的txt
    second_file = file_dir_list[0]  # 待删除子串的txt
    output_file = file_dir_list[1]  # 输出保存的新txt
    # ============================================
    # 1. 处理第一个文本，生成规则列表
    content_list = process_first_txt(first_file)
    # 2. 读取第二个文本为完整字符串
    s = read_second_txt_to_str(second_file)
    # 3. 批量删除列表中所有匹配子串
    new_s = remove_all_substr(s, content_list)
    # 4. 保存到新文件
    save_str_to_txt(new_s, output_file)
    print("处理完成！已保存到", output_file)
if __name__ == "__main__":
    pass
