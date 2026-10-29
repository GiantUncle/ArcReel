"""공급자 레지스트리 메타데이터에 대한 한국어 번역."""

MESSAGES: dict[str, str] = {
    # Provider display names
    "provider_name_gemini-aistudio": "AI Studio",
    "provider_name_gemini-vertex": "Vertex AI",
    "provider_name_ark": "Volcengine Ark",
    "provider_name_ark-agent-plan": "Volcengine Ark Agent Plan",
    "provider_name_grok": "Grok",
    "provider_name_openai": "OpenAI",
    "provider_name_vidu": "Vidu",
    "provider_name_dashscope": "Alibaba Model Studio",
    "provider_name_minimax": "MiniMax",
    "provider_name_kling": "Kling",
    "provider_name_agnes": "Agnes",
    # 失败文案里目录查不到的供应商（已被删除）的泛称
    "deleted_provider_display_name": "삭제된 공급자",
    "deleted_agent_provider_display_name": "삭제된 Agent 공급자",
    # Provider descriptions
    "provider_desc_gemini-aistudio": "Google AI Studio는 이미지, 영상, 음성 생성 기능을 갖춘 Gemini 모델을 제공하며, 빠른 프로토타이핑과 개인 프로젝트에 적합합니다.",
    "provider_desc_gemini-vertex": "Google Cloud Vertex AI 엔터프라이즈 플랫폼. Gemini와 Imagen 모델을 더 높은 할당량과 오디오 생성과 함께 지원합니다.",
    "provider_desc_ark": "ByteDance의 Volcengine Ark AI 플랫폼. Seedance 영상 생성과 Seedream 이미지 생성을 지원하며, 오디오와 seed 제어를 제공합니다.",
    "provider_desc_ark-agent-plan": "Volcengine Ark Agent Plan은 Doubao 등 주요 모델을 한데 모아 텍스트, 이미지, 영상 생성을 지원합니다.",
    "provider_desc_grok": "영상과 이미지 생성을 지원하는 xAI Grok 모델.",
    "provider_desc_openai": "GPT-5.4 텍스트와 GPT Image 생성을 지원하는 OpenAI 플랫폼.",
    "provider_desc_vidu": "Shengshu Vidu 영상 플랫폼. 텍스트-영상, 이미지-영상, 첫-끝 프레임, 참조-영상, 참조-이미지 생성을 지원합니다. 이미지와 영상만 지원합니다.",
    "provider_desc_dashscope": "Alibaba Cloud Model Studio (DashScope) 전 모달리티 플랫폼. Qwen 텍스트, Qwen-Image / Wan 이미지, HappyHorse / Wan 영상(참조-영상 포함)을 지원합니다.",
    "provider_desc_minimax": "MiniMax (Hailuo) 멀티모달 플랫폼. 텍스트, 이미지, 영상, 음성 생성을 지원합니다. 기본적으로 중국 내 사이트에 연결되며, 해외에서 쓰려면 base_url을 국제 사이트로 설정하세요.",
    "provider_desc_kling": "Kuaishou Kling 영상 및 이미지 생성 플랫폼. API Key 인증은 모든 모델에서 동작하고, Access Key + Secret Key (JWT)는 3.0 이하 모델만 지원합니다. 둘 중 하나를 선택하세요. 둘 다 설정하면 API Key가 우선합니다.",
    "provider_desc_agnes": "Agnes 멀티모달 플랫폼 (OpenAI 방식). Bearer API 키로 인증하며, 현재 이미지, 텍스트, 영상 생성을 지원합니다.",
    # Agent preset notes (lib/agent/agent_provider_catalog.py)
    "preset_notes_deepseek": "DeepSeek 공식 Anthropic 호환 엔드포인트. sk- 접두사가 붙은 키가 필요합니다.",
    "preset_notes_xiaomi_mimo": "Xiaomi MiMo는 알려진 모델 이름만 받으며, 공개된 모델 목록이 없습니다.",
    "preset_notes_ark_coding_plan": "Volcengine Ark Coding Plan. 모델 목록 엔드포인트가 없으므로, Ark 콘솔에서 활성화해 둔 추천 모델을 선택하세요.",
    "preset_notes_ark_agent_plan": "Volcengine Ark Agent Plan. 모델 목록 엔드포인트가 없으므로, 요금제에 포함된 추천 모델을 선택하세요.",
}
