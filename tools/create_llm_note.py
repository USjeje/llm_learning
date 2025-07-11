import os

def create_llm_note(tag, title, year_dir, image_name=None, paper_link=None):
    # 生成文件路径
    docs_dir = f"docs/{year_dir}"
    os.makedirs(docs_dir, exist_ok=True)
    md_path = os.path.join(docs_dir, f"{tag}.md")
    
    # 图片路径示例
    image_block = ""
    if image_name:
        image_block = f"![模型结构](../../assets/images/models/{image_name})\n"
    
    # 论文链接
    paper_block = ""
    if paper_link:
        paper_block = f"- **论文链接**: [{title}]({paper_link})\n"
    
    # 模板内容
    content = f"""# {tag} - {title}

## 📋 基本信息
- **标签**: {tag}
- **标题**: {title}
{paper_block}

## 🧩 技术背景
简要介绍背景。

## 💡 核心思想
简要描述核心思想。

## 🔬 技术细节
{image_block}
- 公式示例：  
  $$
  y = x + 1
  $$

## 📊 影响评估
简要描述影响。

## 📚 相关资源
- [论文原文]({paper_link if paper_link else 'https://arxiv.org/'})
- [代码实现](https://github.com/)
- [讲解视频](https://www.bilibili.com/)

## 📝 个人笔记
写下你的理解、收获、疑问等。

---
*最后更新: 2024年7月*
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"已生成：{md_path}")

# 示例用法
if __name__ == "__main__":
    create_llm_note(
        tag="2017-Transformer",
        title="Attention is All You Need",
        year_dir="2017-2018",
        image_name="transformer-arch.png",
        paper_link="https://arxiv.org/abs/1706.03762"
    )