import os
import re
import json
import time
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

# 1. تهيئة النواة المركزية الخارقة V10
app = FastAPI(title="Quantum Nexus OS - V10 Absolute Overlord")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. هيكلة الكون الكمومي والأرشفة اللحظية
BASE_DIR = "Quantum_Universe"
AGENT_FOLDERS = {
    "code": f"{BASE_DIR}/Code_Nexus",
    "video": f"{BASE_DIR}/Cinema_Studio",
    "music": f"{BASE_DIR}/Sonic_Labs",
    "writing": f"{BASE_DIR}/Creative_Ink"
}

for folder in AGENT_FOLDERS.values():
    os.makedirs(folder, exist_ok=True)

MEMORY_FILE = f"{BASE_DIR}/quantum_memory_v10.json"
if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump({}, f)

def load_context(agent_type):
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            memory = json.load(f)
        return memory.get(agent_type, [])
    except:
        return []

def save_context(agent_type, user_prompt, ai_response):
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            memory = json.load(f)
        if agent_type not in memory:
            memory[agent_type] = []
        memory[agent_type].append({"user": user_prompt, "assistant": ai_response})
        memory[agent_type] = memory[agent_type][-5:] # ذاكرة أعمق ممتدة لـ 5 محادثات كاملة بالسياق
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(memory, f, ensure_ascii=False, indent=4)
    except:
        pass

# 3. محرك الاستخلاص والفرز البرمجي المتعدد الذكي لـ V10
def extract_and_save_all_codes(content, target_folder):
    code_blocks = re.findall(r'```(\w+)\n(.*?)```', content, re.DOTALL)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # خريطة للامتدادات الذكية
    ext_map = {
        'python': 'py', 'py': 'py',
        'javascript': 'js', 'js': 'js',
        'typescript': 'ts', 'ts': 'ts',
        'html': 'html', 'css': 'css',
        'json': 'json', 'bash': 'sh', 'sh': 'sh'
    }
    
    for count, (ext, code) in enumerate(code_blocks, 1):
        file_ext = ext_map.get(ext.lower(), 'txt')
        code_file = f"{target_folder}/Quantum_System_{timestamp}_{count}.{file_ext}"
        with open(code_file, "w", encoding="utf-8") as f:
            f.write(code.strip())

# 4. تراكيب الطلبات
class AgentRequest(BaseModel):
    agent_type: str
    prompt_used: str

@app.post("/api/agent/run")
async def run_quantum_overlord_agent(request: AgentRequest):
    groq_api_key = "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"
    
    # 🧠 برومبت V10: تفعيل المناظرة الداخلية والتحقق الذاتي الصارم قبل الإجابة
    v10_meta_prompt = (
        "CRITICAL V10 PROTOCOL: You operate as a unified cluster of dual AI entities: 'The Creative Quantum Architect' and 'The Hardcore Code/Content Reviewer'. "
        "Before delivering the final output, the Architect proposes the solution, the Reviewer aggressively finds flaws, bugs, or missing edge cases, and then you synthesize the ultimate flawless response. "
        "Format everything beautifully using advanced Markdown, including bold headers, clean blockquotes, and tables where applicable."
    )

    system_prompts = {
        "code": f"{v10_meta_prompt} You are the Absolute Quantum Code Overlord. Provide enterprise-grade clean architecture. Wrap all executable script blocks strictly in standard markdown (e.g. ```python ... ```). Ensure no logical bugs exist.",
        "video": f"{v10_meta_prompt} You are the Legendary Cinematic Director. Output detailed master scripts split into technical tables: scene number, focal lengths, lighting setups, soundscapes, and advanced prompts for AI generative tools.",
        "music": f"{v10_meta_prompt} You are the Master AI Audio Composer & Acoustic Physicist. Provide professional arrangements, exact BPM, scale keys, progression layers, and highly specific text-to-audio prompts.",
        "writing": f"{v10_meta_prompt} You are the Infinite Knowledge Mind. Generate high-end, deeply researched professional text using structured Markdown layouts."
    }
    
    selected_system = system_prompts.get(request.agent_type, f"{v10_meta_prompt} You are a Master Quantum AI.")
    
    # استدعاء الذاكرة التراكمية الممتدة
    history = load_context(request.agent_type)
    messages = [{"role": "system", "content": selected_system}]
    for chat in history:
        messages.append({"role": "user", "content": chat["user"]})
        messages.append({"role": "assistant", "content": chat["assistant"]})
    messages.append({"role": "user", "content": request.prompt_used})

    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {groq_api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": messages,
            "temperature": 0.58, # درجة حرارة مثالية متوازنة تماماً للحفاظ على الإبداع مع تصفير نسبة الأخطاء البرمجية
            "top_p": 0.90
        }
        
        # رصد القياسات عن بعد (Telemetry)
        start_time = time.time()
        response = requests.post(url, json=payload, headers=headers)
        end_time = time.time()
        
        execution_time = round((end_time - start_time), 3)

        if response.status_code == 200:
            result_data = response.json()
            ai_response_text = result_data['choices'][0]['message']['content']
            
            tokens_output = result_data.get('usage', {}).get('completion_tokens', 1)
            tokens_per_second = round(tokens_output / execution_time if execution_time > 0 else tokens_output, 1)

            # كتابة ملف الأرشيف الكلي بصيغة الـ Markdown الاحترافية
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            agent_folder = AGENT_FOLDERS.get(request.agent_type, BASE_DIR)
            md_filename = f"{agent_folder}/Overlord_Output_{timestamp}.md"
            with open(md_filename, "w", encoding="utf-8") as f:
                f.write(f"# QUANTUM V10 MASTER REPORT - {timestamp}\n\n{ai_response_text}")
            
            # استخراج شامل وفوري لكل الملفات البرمجية النظيفة أياً كان عددها ولغاتها
            if request.agent_type == "code":
                extract_and_save_all_codes(ai_response_text, agent_folder)
            
            # حفظ الجلسة في الذاكرة التراكمية
            save_context(request.agent_type, request.prompt_used, ai_response_text)
            
            return {
                "status": "success",
                "ai_response": ai_response_text,
                "telemetry": {
                    "execution_time_sec": execution_time,
                    "tokens_per_second": tokens_per_second,
                    "quantum_layer": "V10 Overlord Engine",
                    "saved_at": md_filename
                }
            }
        else:
            return {"status": "error", "message": f"Groq Overlord Alert: {response.text}"}

    except Exception as e:
        return {"status": "error", "message": f"Critical V10 Exception: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5050, reload=True)