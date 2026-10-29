import type enEvents from '../en/events';

export default {
  "label.grid": '멀티 그리드 스토리보드 "{{id}}"',
  "label.grid_split": '멀티 그리드 스토리보드 "{{id}}" 분할',
  "label.voice_sample": '"{{id}}"의 보이스 샘플',
  "label.asset_image_character": '캐릭터 "{{id}}"의 에셋 이미지',
  "label.asset_image_scene": '장면 "{{id}}"의 에셋 이미지',
  "label.asset_image_prop": '소품 "{{id}}"의 에셋 이미지',
  "label.asset_image_product": '상품 "{{id}}"의 에셋 이미지',
  "label.asset_image_character_derivative": '캐릭터 파생 "{{id}}"의 에셋 이미지',
  "label.skeleton_segments": '세그먼트 "{{id}}"',
  "label.skeleton_scenes": '장면 "{{id}}"',
  "label.skeleton_shots": '샷 "{{id}}"',
  "label.skeleton_video_units": '비디오 유닛 "{{id}}"',
  "label.narration_audio": '내레이션 오디오 "{{id}}"',
  "label.named_entity_character": '캐릭터 "{{id}}"',
  "label.named_entity_scene": '장면 "{{id}}"',
  "label.named_entity_prop": '소품 "{{id}}"',
  "label.named_entity_product": '상품 "{{id}}"',
  "label.named_entity_character_derivative": '캐릭터 파생 "{{id}}"',
  "label.character_reference_audio": '캐릭터 "{{id}}"의 참조 오디오',
  "label.project_settings": "프로젝트 설정",
  "label.overview": "프로젝트 개요",
  "label.episode": "{{episode_name}}",
  "label.draft_normalized_script": "{{episode_name}}의 정규화된 대본",
  "label.draft_segment_splitting": "{{episode_name}}의 세그먼트 분할",
  "label.draft_script_plan": "{{episode_name}}의 대본 계획 초안",
  "label.draft_prompt_authoring": "{{episode_name}}의 프롬프트 작성 초안",

  "entity.project": "프로젝트",
  "entity.character": "캐릭터",
  "entity.scene": "장면",
  "entity.prop": "소품",
  "entity.product": "상품",
  "entity.segment": "세그먼트",
  "entity.drama_scene": "장면",
  "entity.shot": "샷",
  "entity.reference_unit": "비디오 유닛",
  "entity.episode": "에피소드",
  "entity.overview": "프로젝트 개요",
  "entity.draft": "대본 계획 결과",
  "entity.grid": "멀티 그리드 스토리보드",
  "entity.task": "작업",
  "entity.fallback": "항목",

  "noun.storyboard_image": "스토리보드 이미지",
  "noun.video": "비디오",
  "noun.grid": "멀티 그리드 스토리보드",
  "noun.narration_audio": "내레이션 오디오",
  "noun.voice_sample": "보이스 샘플",

  "single.storyboard_ready": "{{label}}의 스토리보드 이미지가 준비되었습니다",
  "single.video_ready": "{{label}}의 비디오가 준비되었습니다",
  "single.generated": "{{label}}이(가) 준비되었습니다",
  "single.completed": "{{label}}이(가) 완료되었습니다",
  "single.created": "{{label}}이(가) 추가되었습니다",
  "single.deleted": "{{label}}이(가) 삭제되었습니다",
  "single.updated": "{{label}}이(가) 업데이트되었습니다",

  "deferred.storyboard_ready":
    "AI가 {{label}}의 스토리보드 이미지를 방금 생성했습니다. 눌러서 보기",
  "deferred.video_ready":
    "AI가 {{label}}의 비디오를 방금 생성했습니다. 눌러서 보기",
  "deferred.generated": "{{label}}이(가) 준비되었습니다",
  "deferred.completed": "{{label}}이(가) 완료되었습니다",
  "deferred.created": "AI가 {{label}}을(를) 방금 추가했습니다. 눌러서 보기",
  "deferred.deleted": "AI가 {{label}}을(를) 방금 삭제했습니다. 눌러서 보기",
  "deferred.updated": "AI가 {{label}}을(를) 방금 업데이트했습니다. 눌러서 보기",

  "group.generated": "{{entity}} {{count}}개를 생성했습니다: {{summary}}",
  "group.created": "{{entity}} {{count}}개를 추가했습니다: {{summary}}",
  "group.deleted": "{{entity}} {{count}}개를 삭제했습니다: {{summary}}",
  "group.updated": "{{entity}} {{count}}개를 업데이트했습니다: {{summary}}",

  "group_deferred.generated":
    "AI가 {{entity}} {{count}}개를 방금 생성했습니다: {{summary}}. 눌러서 보기",
  "group_deferred.created":
    "AI가 {{entity}} {{count}}개를 방금 추가했습니다: {{summary}}. 눌러서 보기",
  "group_deferred.deleted":
    "AI가 {{entity}} {{count}}개를 방금 삭제했습니다: {{summary}}. 눌러서 보기",
  "group_deferred.updated":
    "AI가 {{entity}} {{count}}개를 방금 업데이트했습니다: {{summary}}. 눌러서 보기",

  "list.separator": ", ",
  "list.more_suffix": " 외 더 많은 항목",
} satisfies Record<keyof typeof enEvents, string>;
