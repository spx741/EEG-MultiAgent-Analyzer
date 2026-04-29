import json
import os
from openai import OpenAI
from tools.matlab_bridge import MatlabBridge
from eeg_agents.agent_prompts import (
    PREPROCESSING_AGENT_PROMPT, 
    REASONING_AGENT_PROMPT, 
    VISUALIZATION_AGENT_PROMPT
)

class EEGMultiAgentSystem:
    def __init__(self):
        # 确保你在环境变量中设置了 OPENAI_API_KEY，或替换为其他模型API
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "dummy_key"))
        self.matlab = MatlabBridge()

    def _call_llm(self, system_prompt: str, user_input: str) -> str:
        """通用 LLM 调用接口"""
        # 如果没有真实 API key，这里做模拟返回以保证代码可运行演示
        if self.client.api_key == "dummy_key":
            return "{\"status\": \"mocked_response\", \"message\": \"API Key not set.\"}"
            
        response = self.client.chat.completions.create(
            model="gpt-4-turbo", # 或使用适合的开源模型
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content

    def run_pipeline(self, subject_data_path: str):
        print(f"🚀 启动自动化分析管线，目标数据: {subject_data_path}")
        print("-" * 50)

        # 1. 预处理 Agent 介入
        print("🤖 [Agent 1: 预处理] 正在分析数据特征并生成微状态提取参数...")
        prep_params = self._call_llm(PREPROCESSING_AGENT_PROMPT, f"分析路径: {subject_data_path}")
        
        # 调用底层工具 (模拟)
        self.matlab.run_script("run_preprocessing", target=subject_data_path, method="kmeans_microstate")
        
        # 2. 推理 Agent 介入
        print("\n🤖 [Agent 2: 算法推理] 正在构建 DK68 溯源与高阶超图网络模型...")
        reasoning_params = self._call_llm(REASONING_AGENT_PROMPT, "预处理完成，生成超图网络参数。")
        
        # 调用底层工具 (模拟)
        self.matlab.run_script("build_hypergraph", atlas="DK68", network_type="edge_multilayer")

        # 3. 可视化 Agent 介入
        print("\n🤖 [Agent 3: 可视化与汇报] 正在生成学术图表指令与最终汇报...")
        report = self._call_llm(VISUALIZATION_AGENT_PROMPT, "网络构建完毕，请生成总结报告。")
        
        self.matlab.run_script("generate_figures", format="high_res_tiff")

        print("-" * 50)
        print("✅ 自动化流程执行完毕。")
        # print("📝 最终报告预览:\n", report)
