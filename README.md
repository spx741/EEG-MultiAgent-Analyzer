# EEG-MultiAgent-Analyzer 🧠🤖

An AI-driven Multi-Agent system for automated EEG neuroimaging, microstate analysis, and high-order brain network (Hypergraph) construction.

## 🌟 Overview
Traditional EEG processing involves heavy manual parameter tuning and software switching (EEGLAB, Brainstorm). This project implements a three-layer Multi-Agent architecture to automate the workflow from raw data preprocessing to edge-centric multilayer network construction and scientific reporting.

## 🏗️ Architecture
1. **Preprocessing Agent**: Parses raw EEG, identifies channels, and automates microstate sequence segmentation (Classes A/B/C/D).
2. **Reasoning Agent**: Generates parameters and dynamically calls MATLAB scripts for source localization (DK68 atlas) and hypergraph construction.
3. **Visualization Agent**: Evaluates generated network features and compiles publication-ready charts and structured reports.

## 🚀 Quick Start
```bash
git clone [https://github.com/yourusername/EEG-MultiAgent-Analyzer.git](https://github.com/yourusername/EEG-MultiAgent-Analyzer.git)
cd EEG-MultiAgent-Analyzer
pip install -r requirements.txt
export OPENAI_API_KEY="your_api_key_here"
python main.py
