# 原版脚本有错
# 当题干中包含空格和字母，他会解析错误，把题干部分字母解析到选项里
# 此脚本修复了bug
import tkinter as tk
from tkinter import filedialog
import re, time, random, json

root = tk.Tk()
root.withdraw()

# 获取选择好的文件  读取文件
filePath = filedialog.askopenfilename(filetypes=[('txt', '*.txt')])
f = open(filePath, 'r', encoding='UTF-8')
data = f.read()
data = data.replace('．', '.')
f.close()

# 不同题目分割
pattern = re.compile(r'(?:^|\n\s*)\d+?[\.\。]')
data = pattern.split(data)

result = []
for i in data:
    # 使用更精确的选项匹配模式
    option = re.findall(r'\n\s*([A-E])[\.\:\：]\s*(.+?)(?=\n|$)', i)
    # 分离选项字母和内容
    option_clean = [f"{item[1].strip()}" for item in option] if option else []
    
    # 提取题目 - 从开头到第一个选项或答案出现的位置
    title_end_match = re.search(r'(\n\s*[A-E][\.\:\：]|答案[:：])', i)
    title_end = title_end_match.start() if title_end_match else len(i)
    title = i[:title_end].strip()
    
    # 答案提取保持不变
    daan = re.findall(r'答案[:：]([A-E]+)[\n]?', i)
    analysis = ''
    if len(daan) == 0:
        daan = re.findall(r'答案[:：]([\s\S]+)', i)
        if len(daan):
            pattern = re.compile(r'解析[:：]')
            daanList = pattern.split(daan[0])
            if len(daanList) > 1:
                analysis = daanList[1]
                daan = [daanList[0]]
    else:
        jiexi = re.findall(r'解析[:：]([\s\S]+)', i)
        analysis = jiexi[0] if len(jiexi) else ''
    daan = daan[0] if len(daan) else ''

    # 添加到结果
    result.append({
        'id': time.strftime("%Y%m%d%H%M", time.localtime()) + str(random.randint(0, 1000000)),
        'title': title,
        'option': option_clean,
        'answer': daan,
        'analysis': analysis.strip()
    })

# 移除第一个空元素
if result and not result[0]['title']:
    del(result[0])

# 保存结果
f = open(time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.json', 'w', encoding='utf-8')
f.write(json.dumps(result, ensure_ascii=False, indent=4))
f.close()
print("执行完成")