<div align="center">
  <p>
    <a href="https://github.com/WillGasser/FoldEquity" target="_blank">
      <img width="100%" src="https://raw.githubusercontent.com/yourusername/FoldEquity/main/assets/banner.png" alt="FoldEquity banner"></a>
  </p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/FoldEquity)](https://github.com/yourusername/FoldEquity/stargazers)
[![Discord](https://img.shields.io/discord/your-discord-channel?logo=discord)](https://discord.gg/your-invite-link)

<div>
    <a href="https://github.com/yourusername/FoldEquity/actions"><img src="https://github.com/yourusername/FoldEquity/actions/workflows/ci.yml/badge.svg" alt="CI/CD"></a>
    <a href="https://pypi.org/project/FoldEquity/"><img src="https://img.shields.io/pypi/v/FoldEquity" alt="PyPI Version"></a>
    <a href="https://hub.docker.com/r/yourdocker/FoldEquity"><img src="https://img.shields.io/docker/pulls/yourdocker/FoldEquity" alt="Docker Pulls"></a>
</div>
<br>

**FoldEquity** is an AI-powered poker assistant that combines computer vision, reinforcement learning, and game theory to analyze poker tables and make optimal decisions in real time. Built for educational purposes, it demonstrates advanced CV/ML techniques for game automation.

<a href="https://github.com/yourusername/FoldEquity">
  <img width="100%" src="https://raw.githubusercontent.com/yourusername/FoldEquity/main/assets/demo.gif" alt="FoldEquity demo">
</a>
</div>

## <div align="center">Documentation</div>

See below for quickstart instructions. Full documentation available at [docs.FoldEquity.ai](https://docs.FoldEquity.ai).

<details open>
<summary>Installation</summary>

# From Source
    ```bash
    git clone https://github.com/WillGasser/PokerVision.git
    cd PokerVision
    pip install -r requirements.txt

    conda create -n pokervision python=3.10
    conda activate pokervision
    conda install -c conda-forge ultralytics
    pip install pokervision

### Prerequisites
- **Tesseract OCR** (Required for text extraction):
  ```bash
  # Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki
  # Mac:
  brew install tesseract
  # Linux:
  sudo apt-get install tesseract-ocr


  # PyPI (Recommended)
    pip install ultralytics opencv-python pytesseract  # Core dependencies
    pip install pokervision

