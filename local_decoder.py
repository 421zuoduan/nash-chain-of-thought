from transformers import AutoModelForCausalLM, AutoTokenizer
import pickle

import torch

import os
import openai

class custom_api(object):
    def __init__(self,tokenizer_path=None
                     ,pretrained_model=None
                     ,device="cuda"):
        self.device = device
        try:
            self.tokenizer=AutoTokenizer.from_pretrained(tokenizer_path,
                                                         trust_remote_code=True)
        except:
            self.tokenizer = pickle.load(open(tokenizer_path,'rb'))
        
        self.model = AutoModelForCausalLM.from_pretrained(pretrained_model)
        self.model.to(self.device)

    def inference(self,messages,max_new_tokens=256):
        encodeds = self.tokenizer.apply_chat_template(messages, return_tensors="pt")
        model_inputs = encodeds.to(self.device)
        generated_ids = self.model.generate(model_inputs, max_new_tokens=max_new_tokens, do_sample=True)
        decoded = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        #return decoded[0].split('[/INST]')[-1].strip('</s>')
        return decoded[0]

    def inference_raw(self,messages):
        encodeds = self.tokenizer.apply_chat_template(messages, return_tensors="pt")
        model_inputs = encodeds.to(self.device)
        generated_ids = self.model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
        decoded = self.tokenizer.batch_decode(generated_ids)
        return decoded
    

class custom_api_gpt(object):
    def __init__(self, device="cuda", api_key=None):
        """
        初始化GPT-3.5-turbo API调用类
        
        参数说明 (兼容原接口但部分参数未使用):
        - device:          保留参数 (未使用)
        - api_key:         OpenAI API密钥 (优先使用参数，其次环境变量)
        """
        # 处理API密钥
        self.api_key = api_key or os.getenv("CHATANYWHERE_API_KEY")
        if not self.api_key:
            raise ValueError("API key required. Set via api_key parameter or OPENAI_API_KEY environment variable")
        
        # 设置模型名称 (允许通过pretrained_model参数覆盖)
        self.model_name = "gpt-3.5-turbo-0125"
        
        # 配置OpenAI客户端
        openai.api_key = self.api_key

    def inference(self, messages, max_new_tokens=256):
        """
        调用GPT-3.5-turbo生成回复
        
        参数对齐原接口:
        - messages:       对话历史 (格式: [{"role": "user", "content": ...}])
        - max_new_tokens: 最大生成token数 (对应API的max_tokens)
        
        返回: 生成的文本 (自动去除首尾空白)
        """

        client = openai.OpenAI(
            api_key=self.api_key,
            base_url="https://api.chatanywhere.tech/v1"
        )

        response = client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            max_tokens=max_new_tokens,
            temperature=0.7,    # 控制随机性 (0-2)
            top_p=0.9            # 核采样阈值 (0-1)
        )
        return response.choices[0].message.content.strip()

    def inference_raw(self, messages):
        """保持与原接口兼容的长文本生成方法"""
        return self.inference(messages, max_new_tokens=1000)


class custom_api_others(object):
    def __init__(self,tokenizer_path=None
                     ,pretrained_model=None
                     ,device="cuda"):
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(pretrained_model,
                                                       trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(pretrained_model,
                                                          trust_remote_code=True)
        self.model.to(self.device)

    def inference(self,messages,max_new_tokens=256):
        encodeds = self.tokenizer.apply_chat_template(messages, return_tensors="pt")
        model_inputs = encodeds.to(self.device)
        generated_ids = self.model.generate(model_inputs, max_new_tokens=max_new_tokens, do_sample=True)
        decoded = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        return decoded[0]

    def inference_raw(self,messages):
        encodeds = self.tokenizer.apply_chat_template(messages, return_tensors="pt")
        model_inputs = encodeds.to(self.device)
        generated_ids = self.model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
        decoded = self.tokenizer.batch_decode(generated_ids)
        return decoded


    def inference_parallel(self,messages):
        encodeds = self.tokenizer.apply_chat_template(messages, return_tensors="pt")
        model_inputs = encodeds.to(self.device)
        generated_ids = self.model.generate(model_inputs, max_new_tokens=256, do_sample=True)
        decoded = self.tokenizer.batch_decode(generated_ids)
        return [decoded[i_].strip('<|end_of_turn|>') for i_ in range(len(decoded))]



