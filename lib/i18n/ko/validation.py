"""검증 및 아카이브 진단 메시지 (한국어)."""

MESSAGES = {
    # ---- passthrough ----
    "val_literal": "{text}",
    # ---- generic field shape ----
    "val_missing_field": "필수 필드가 누락되었습니다: {field}",
    "val_missing_field_at": "{prefix}: 필수 필드 {field}이(가) 누락되었습니다",
    "val_field_type_string": "필드 타입 오류: {field} 값은 문자열이어야 합니다",
    "val_field_type_bool": "필드 타입 오류: {field} 값은 불리언이어야 합니다",
    "val_field_type_integer": "필드 타입 오류: {field} 값은 정수여야 합니다",
    "val_field_type_number": "필드 타입 오류: {field} 값은 숫자여야 합니다",
    "val_field_out_of_range": "{field} 값 {value}은(는) 허용 범위를 벗어났습니다. {min}에서 {max} 사이여야 합니다",
    "val_field_must_be_string": "{field} 필드는 문자열이어야 합니다",
    "val_field_must_be_string_typed": "{field} 필드는 문자열이어야 합니다. 현재 값: {actual}",
    "val_field_must_be_array": "{field} 필드는 배열이어야 합니다",
    "val_field_must_be_nonempty_array": "{field} 필드는 비어 있지 않은 배열이어야 합니다",
    "val_field_must_be_nonempty_string": "{field} 필드는 비어 있지 않은 문자열이어야 합니다",
    "val_field_must_be_object": "{field} 필드는 객체여야 합니다",
    "val_field_invalid": "{field} 필드가 올바르지 않습니다: {detail}",
    "val_ledger_source_file_not_relative": "source_file은 프로젝트 기준 상대 경로(POSIX)여야 합니다",
    "val_ledger_source_file_escapes": "source_file은 절대 경로일 수 없고 ..을 포함할 수도 없습니다",
    "val_ledger_start_after_end": "start는 end보다 클 수 없습니다",
    "val_field_bad_timestamp": "{field} 필드가 유효한 ISO8601 타임스탬프가 아닙니다: {value}",
    "val_item_must_be_object": "{prefix}: 객체여야 합니다",
    "val_item_format_object": "{prefix}: 데이터 형식이 잘못되었습니다. 객체여야 합니다",
    # ---- path references ----
    "val_path_empty": "{field}: 경로는 비어 있을 수 없습니다",
    "val_path_traversal": "{field}: 참조 경로가 프로젝트 밖으로 벗어납니다: {path}",
    "val_path_outside_dir": "{field}: 참조 경로는 {dir}/ 아래에 있어야 합니다: {path}",
    "val_path_missing": "{field}: 참조된 파일이 존재하지 않습니다: {path}",
    "val_path_must_be_relative": "{field} 필드는 프로젝트 기준 상대 경로여야 합니다: {path}",
    # ---- project-level fields ----
    "val_content_mode_invalid": "content_mode이(가) 올바르지 않습니다: '{value}'. {allowed} 중 하나여야 합니다",
    "val_source_kind_invalid": "{prefix}: source_kind '{value}'이(가) 올바르지 않습니다. {allowed} 중 하나여야 합니다",
    "val_generation_mode_invalid": "generation_mode이(가) 올바르지 않습니다: '{value}'. {allowed} 중 하나여야 합니다",
    "val_deprecated_clues": (
        "project.json에 지원이 중단된 필드 clues가 포함되어 있습니다. "
        "자동 마이그레이션을 기다리거나 서비스를 재시작해 주세요"
    ),
    "val_deprecated_field_removable": "{field} 필드는 지원이 중단되었고(읽을 때 계산됨) 안전하게 삭제할 수 있습니다",
    "val_cannot_load_project_json": "project.json을 불러올 수 없습니다: {path}",
    "val_cannot_load_script": "대본 파일을 불러올 수 없습니다: {path}",
    "val_unrecognized_entry": "인식할 수 없는 추가 파일/디렉터리가 발견되었습니다: {name}",
    "val_novel_must_be_object": "novel 필드는 객체여야 합니다",
    # ---- episode entries and ledger ----
    "val_ledger_status_type": "{prefix}: ledger_status는 문자열이어야 합니다. 현재 값: {value}",
    "val_source_origin_invalid": "{prefix}: source_origin '{value}'이(가) 올바르지 않습니다. {allowed} 중 하나여야 합니다",
    "val_source_range_requires_whole_source": "{prefix}: source_range는 원본 전체에서 잘라낸 에피소드(source_origin whole_source)에만 설정할 수 있습니다",
    "val_whole_source_file_invalid": "whole_source_files[{index}]는 source_file이 source/ 바로 아래의 .txt 또는 .md 파일을 가리키는 객체여야 합니다",
    "val_episode_missing_num_at": "{prefix}: 필수 필드가 누락되었습니다: episode(정수)",
    "val_episode_missing_title_at": "{prefix}: 필수 필드가 누락되었습니다: title(문자열, 비어 있어도 됨)",
    "val_episode_missing_num": "필수 필드가 누락되었습니다: episode(정수)",
    # ---- ad / short-film projects ----
    "val_ad_only_field": "{field} 필드는 광고/단편 프로젝트(content_mode=ad)에서만 사용할 수 있습니다",
    "val_ad_missing_target_duration": (
        "필수 필드가 누락되었습니다: target_duration(광고/단편 프로젝트의 목표 전체 길이, 초 단위)"
    ),
    "val_ad_target_duration_invalid": "target_duration이(가) 올바르지 않습니다: {value}. 양의 정수(초)여야 합니다",
    "val_ad_no_default_duration": (
        "광고/단편 프로젝트는 default_duration을 사용하지 않습니다 "
        "(샷 길이는 target_duration을 기준으로 샷별로 배분합니다)"
    ),
    "val_ad_no_episode_target_duration": (
        "광고/단편 프로젝트는 episode_target_duration을 사용하지 않습니다 "
        "(에피소드 전체 길이는 target_duration을 기준으로 배분합니다)"
    ),
    "val_ad_no_grid_storyboard": "광고/단편 프로젝트는 멀티 그리드 스토리보드(grid_storyboard)를 지원하지 않습니다",
    "val_ad_episodes_single": "광고/단편 프로젝트는 항상 에피소드 항목을 정확히 하나만 가져야 합니다(에피소드 1)",
    "val_ad_shots_missing": "광고 대본에 shots 배열이 없습니다",
    "val_ad_duration_drift": (
        "대본 총 길이 {total}초는 target_duration {target}초와 {delta:.0%} 차이가 나며, "
        "{threshold:.0%} 관찰 기준을 벗어났습니다(참고용이며 저장은 차단되지 않습니다)"
    ),
    # ---- asset catalogs ----
    "val_asset_format_object": "{asset_type} '{name}'의 데이터 형식이 잘못되었습니다. 객체여야 합니다",
    "val_asset_field_must_be_object": "{asset_type} '{name}'.{field} 필드는 객체여야 합니다",
    "val_asset_field_must_be_string": "{asset_type} '{name}'.{field} 필드는 문자열이어야 합니다. 현재 값: {actual}",
    "val_asset_field_bad_timestamp": "{asset_type} '{name}'.{field} 필드가 유효한 ISO8601 타임스탬프가 아닙니다: {value}",
    "val_asset_field_must_be_string_list": "{asset_type} '{name}'.{field} 필드는 문자열 목록이어야 합니다. 현재 값: {actual}",
    "val_asset_field_item_must_be_string": "{asset_type} '{name}'.{field}[{index}] 항목은 문자열이어야 합니다. 현재 값: {actual}",
    "val_asset_name_duplicate": (
        "프로젝트 에셋 이름이 중복되었습니다: {duplicate_type} '{duplicate_name}'이(가) "
        "strip + Unicode NFC 정규화 후 {first_type} '{first_name}'과(와) 충돌합니다"
    ),
    # ---- item-level references ----
    "val_refs_unregistered": "{prefix}: {field} 필드가 project.json에 없는 {asset_type} 항목을 참조합니다: {names}",
    "val_missing_defaults_empty_array": "{prefix}: {field} 필드가 누락되어 빈 배열로 처리합니다",
    # ---- generic item checks ----
    "val_id_format": "{prefix}: {field} 형식 '{value}'이(가) 올바르지 않습니다. E{{n}}S{{nn}} 형식이어야 합니다",
    "val_missing_duration_default": "{prefix}: duration_seconds가 누락되어 기본값 {default}을(를) 사용합니다",
    "val_duration_invalid": "{prefix}: duration_seconds '{value}'이(가) 올바르지 않습니다. 양의 정수여야 합니다",
    # ---- drama utterances ----
    "val_utterance_must_be_object": "{prefix} 항목은 객체여야 합니다",
    "val_utterance_kind_invalid": "{prefix}의 kind는 dialogue 또는 voiceover여야 합니다",
    "val_utterance_text_invalid": "{prefix}의 text는 비어 있지 않은 문자열이어야 합니다",
    "val_utterance_speaker_type": "{prefix}의 speaker는 문자열 또는 null이어야 합니다",
    "val_utterance_dialogue_speaker": "{prefix}의 dialogue에는 비어 있지 않은 speaker가 있어야 합니다",
    "val_utterance_voiceover_speaker": "{prefix}의 voiceover에는 speaker를 둘 수 없습니다",
    "val_scene_speech_overflow": (
        "{prefix}: 예상 대사 길이는 {spoken:.1f}초로, {duration}초 장면 길이를 {tolerance:.0%} 넘게 초과합니다 "
        "(허용 상한 {budget:.1f}초). 긴 대사는 맞지 않거나 답답하게 들릴 수 있습니다 "
        "(참고용이며 저장은 차단되지 않습니다)"
    ),
    # ---- ad shots ----
    "val_shot_duration_missing_zero": "{prefix}: duration_seconds가 누락되어 총합에 0으로 계산됩니다",
    "val_shot_duration_out_of_range": (
        "{prefix}: duration_seconds '{value}'이(가) 올바르지 않습니다. "
        "reference_video 모드에서는 {low}에서 {high} 사이의 정수여야 합니다"
    ),
    "val_shot_missing_voiceover_text": (
        "{prefix}: 필수 필드가 누락되었습니다: voiceover_text(더빙 대사, 비어 있어도 됨)"
    ),
    # ---- reference-video units ----
    "val_unit_id_missing": "{prefix}: unit_id가 누락되었습니다",
    "val_unit_id_missing_required": "{prefix}: 필수 필드가 누락되었습니다: unit_id",
    "val_unit_id_duplicate": "{prefix}: unit_id '{value}'이(가) 중복됩니다",
    "val_video_units_missing": "reference_video 대본에 video_units 배열이 없습니다",
    "val_unit_duration_range": "{prefix}: duration_seconds는 {low}에서 {high} 사이의 정수여야 합니다",
    # ---- skeleton / route mismatch ----
    "val_skeleton_noun_segments": "세그먼트",
    "val_skeleton_noun_scenes": "장면",
    "val_skeleton_noun_shots": "샷",
    "val_skeleton_noun_video_units": "영상 단위",
    "val_route_reference_video": "참조 기반 영상 생성(reference_video)",
    "val_route_storyboard": "스토리보드 기반 영상 생성(storyboard)",
    "val_skeleton_mismatch_reference_known": (
        "대본 골격이 프로젝트 생성 모드와 일치하지 않습니다: 생성 모드는 {route}이며 "
        "{expected}({expected_noun}) 골격이 필요한데, 이 대본은 {actual}({actual_noun})을(를) 사용합니다. "
        "generate_script_plan을 호출해 이 에피소드를 다시 분할한 뒤 대본을 다시 생성해 주세요. "
        "대본은 여전히 조회, 편집, 내보내기할 수 있습니다"
    ),
    "val_skeleton_mismatch_reference_none": (
        "대본 골격이 프로젝트 생성 모드와 일치하지 않습니다: 생성 모드는 {route}이며 "
        "{expected}({expected_noun}) 골격이 필요한데, 이 대본에는 골격 배열이 아예 없습니다. "
        "generate_script_plan을 호출해 이 에피소드를 다시 분할한 뒤 대본을 다시 생성해 주세요. "
        "대본은 여전히 조회, 편집, 내보내기할 수 있습니다"
    ),
    "val_skeleton_mismatch_storyboard_known": (
        "대본 골격이 프로젝트 생성 모드와 일치하지 않습니다: 생성 모드는 {route}이며 "
        "{expected}({expected_noun}) 골격이 필요한데, 이 대본은 {actual}({actual_noun})을(를) 사용합니다. "
        "에피소드 분할(script_plan)을 다시 실행해 이 에피소드를 재분할한 뒤 대본을 다시 생성해 주세요. "
        "대본은 여전히 조회, 편집, 내보내기할 수 있습니다"
    ),
    "val_skeleton_mismatch_storyboard_none": (
        "대본 골격이 프로젝트 생성 모드와 일치하지 않습니다: 생성 모드는 {route}이며 "
        "{expected}({expected_noun}) 골격이 필요한데, 이 대본에는 골격 배열이 아예 없습니다. "
        "에피소드 분할(script_plan)을 다시 실행해 이 에피소드를 재분할한 뒤 대본을 다시 생성해 주세요. "
        "대본은 여전히 조회, 편집, 내보내기할 수 있습니다"
    ),
    # ---- reference-video duration consolidation migration ----
    "val_unit_duration_clamped": (
        "unit {unit_id}의 길이 {target}초는 합리적인 범위 {low}-{high}초를 벗어나 {clamped}초로 조정했습니다"
    ),
    "val_unit_duration_slotted": (
        "unit {unit_id}의 길이 {duration}초는 모델의 길이 옵션({durations})이 아니어서 "
        "{slot}초로 맞췄습니다"
    ),
    # ---- archive repair and import/export diagnostics ----
    "arch_source_encoding_unconverted": (
        "소스 파일 인코딩을 감지하지 못해 UTF-8로 변환하지 않았습니다: source/{name} "
        "(에피소드 기획이 이 파일을 읽을 수 없습니다)"
    ),
    "arch_non_standard_entry_excluded": "비표준 최상위 디렉터리/파일 '{entry}'은(는) 내보내기에서 제외되었습니다",
    "arch_invalid_project_json": "{file}을(를) 구문 분석할 수 없습니다: {path}",
    "arch_version_history_malformed": "{location}: 버전 기록이 예상한 형식이 아닙니다",
    "arch_version_snapshot_path_unmanaged": "{location}: 버전 레코드의 스냅샷 경로가 해당 리소스 타입의 버전 디렉터리 밖에 있습니다",
    "arch_script_file_repaired": "{location}: {path}(으)로 자동 복구했습니다",
    "arch_missing_script_file_pending": "{location}: 대본이 아직 생성되지 않았습니다: {path}",
    "arch_missing_script_file": "{location}: 참조된 파일이 존재하지 않습니다: {path}",
    "arch_invalid_script_json": "대본 파일을 구문 분석할 수 없습니다: {path}",
    "arch_deprecated_source_file_removed": "novel.source_file 필드는 지원이 중단되어 삭제되었습니다",
    "arch_deprecated_field_removed": "{field} 필드는 지원이 중단되어(읽을 때 계산됨) 삭제되었습니다",
    "arch_deprecated_clue_field_removed": (
        "{items_key}[{index}]: 지원이 중단된 필드 {field}을(를) 삭제했습니다(scenes/props를 사용해 주세요)"
    ),
    "arch_missing_field_filled": "{items_key}[{index}]: 누락된 필드 {field}을(를) 채웠습니다",
    "arch_unit_unresolved_mentions": (
        "video_units[{index}]: 본문에 project.json에 없는 에셋 이름이 언급되어 있습니다: {names}. "
        "해당 이름으로는 참조 이미지를 만들지 못합니다"
    ),
    "arch_generated_assets_defaults": "{label}[{index}].generated_assets: 기본 필드 {fields}을(를) 채웠습니다",
    "arch_missing_generated_assets": "{label}[{index}]: 누락된 필드 generated_assets를 채웠습니다",
    "arch_invalid_generated_assets": (
        "{label}[{index}]: generated_assets의 형식이 잘못되어({actual}) 기본 구조로 초기화했습니다"
    ),
    "arch_placeholder_character_added": "누락된 캐릭터 정의를 자동으로 추가했습니다: {name}",
    "arch_placeholder_asset_added": "누락된 {asset_type} 정의를 자동으로 추가했습니다: {name}",
    "arch_canonical_path_normalized": "{location}: {path}(으)로 정규화했습니다",
    "arch_current_asset_materialized": "{location}: {target} 파일을 {source}에서 복원했습니다",
    "arch_current_asset_restored_from_version": "{location}: {target} 파일을 {source}에서 복원했습니다",
    # ---- archive import errors ----
    "arch_invalid_conflict_policy": "충돌 정책이 올바르지 않습니다",
    "arch_conflict_policy_unsupported": "conflict_policy는 prompt, rename, overwrite만 지원합니다. 현재 값: {value}",
    "arch_import_validation_failed": "가져오기 패키지 검증에 실패했습니다",
    "arch_artifact_activation_failed": "가져온 프로젝트의 아티팩트 상태가 일관되지 않습니다: {reason}",
    "arch_project_migration_failed": "아카이브의 프로젝트 데이터를 현재 버전으로 올릴 수 없습니다: {reason}",
    "arch_import_confirmation_required": "아카이브를 업그레이드하면서 일부 내용이 변경되었습니다. 가져오기 전에 확인해 주세요",
    "arch_not_a_zip": "업로드한 파일은 유효한 ZIP 아카이브가 아닙니다",
    "arch_zip_encrypted_entry": "ZIP에 암호화된 항목이 있어 가져올 수 없습니다: {name}",
    "arch_zip_absolute_path_entry": "ZIP에 절대 경로 항목이 있습니다: {name}",
    "arch_zip_traversal_entry": "ZIP에 경로 순회 항목이 있습니다: {name}",
    "arch_zip_symlink_entry": "ZIP에 심볼릭 링크 항목이 있습니다: {name}",
    "arch_zip_unparsable_member": "{label}을(를) 구문 분석할 수 없습니다: {path}",
    "arch_multiple_manifests": (
        "ZIP에 arcreel-export.json 파일이 여러 개 있어 프로젝트 루트를 특정할 수 없습니다"
    ),
    "arch_manifest_missing_project_json": "공식 내보내기 패키지에 project.json이 없습니다",
    "arch_no_project_json": "ZIP에서 project.json을 찾을 수 없습니다",
    "arch_multiple_project_json": "ZIP에 project.json 파일이 여러 개 있어 프로젝트 루트를 특정할 수 없습니다",
    "arch_extract_path_traversal": "압축 해제 경로가 대상 디렉터리를 벗어납니다: {path}",
    "arch_conflict_detected": "프로젝트 ID 충돌이 감지되었습니다",
    "arch_project_name_conflict": (
        "프로젝트 ID '{name}'이(가) 이미 존재합니다. 기존 프로젝트를 덮어쓸지, 새 이름으로 가져올지 선택해 주세요."
    ),
    # ---- Custom endpoint definition validation ----
    "val_ce_missing_field": "필수 필드가 누락되었습니다: {field}",
    "val_ce_unknown_field": "알 수 없는 필드입니다: {field}",
    "val_ce_removed_field": "형식에서 제거된 필드입니다: {field} - {reason}",
    "val_ce_invalid_type": "타입이 올바르지 않습니다. {expected} 타입이어야 합니다",
    "val_ce_invalid_enum_value": "여기서는 이 값을 사용할 수 없습니다. 허용 값: {allowed}",
    "val_ce_invalid_value": "값이 형식과 일치하지 않습니다: {detail}",
    "val_ce_schema_violation": "정의 형식과 일치하지 않습니다: {detail}",
    "val_ce_schema_minimum_constraint": "허용 최솟값: {limit}",
    "val_ce_schema_maximum_constraint": "허용 최댓값: {limit}",
    "val_ce_schema_format_constraint": "요구 형식을 만족하지 않습니다: {constraint}",
    "val_ce_schema_forbidden_constraint": "값이 금지된 제약에 해당합니다",
    "val_ce_schema_generic_constraint": "정의 제약({keyword})을 만족하지 않습니다",
    "val_ce_removed_reason_request_query": (
        "정적/동적 쿼리 파라미터는 url 템플릿에, 자격 증명 쿼리는 auth.query에 넣어야 합니다"
    ),
    "val_ce_removed_reason_status_codes": (
        "HTTP 상태 처리는 런타임 정책입니다: 2xx는 성공, 429와 5xx는 재시도, 그 외는 실패입니다"
    ),
    "val_ce_removed_reason_polling_policy": "폴링 간격과 타임아웃은 정의의 일부가 아니라 런타임 정책입니다",
    "val_ce_removed_reason_extract_source": "추출은 항상 응답 본문에서 시작합니다. HTTP 상태는 경로가 아닙니다",
    "val_ce_removed_reason_extract_usage_keys": "usage는 이제 poll.extract.usage 아래에 있습니다",
    "val_ce_removed_reason_mime_types": "에셋 형식은 허용 목록으로 제한하지 않습니다. 공급자가 받을 수 없는 것은 공급자가 거부합니다",
    "val_ce_removed_reason_comfyui_capabilities": (
        "ComfyUI 엔드포인트의 기능은 노드 바인딩에서 도출되므로 정의에 선언을 두지 않습니다"
    ),
    "val_ce_malformed_placeholder": (
        "{fragment}은(는) 유효한 플레이스홀더가 아닙니다. 변수 이름만 지원합니다 "
        "(예: prompt 또는 inputs.first_frame). 필터, 인덱스, 표현식은 사용할 수 없고, "
        "여는 중괄호는 모두 닫혀 있어야 합니다"
    ),
    "val_ce_undeclared_variable": "플레이스홀더 {name}이(가) 선언되지 않은 변수를 참조합니다",
    "val_ce_api_key_outside_auth": (
        "api_key는 auth 섹션에만 쓸 수 있습니다: 자격 증명은 본문과 URL에 두지 않고, "
        "공유하는 정의에도 두지 않습니다"
    ),
    "val_ce_auth_without_api_key": (
        "auth 섹션이 비어 있지 않은데 api_key를 참조하지 않습니다: 자격 증명 없는 API라면 비워 두고, "
        "그렇지 않다면 자격 증명을 기록하도록 만들어 주세요"
    ),
    "val_ce_auth_header_conflict": (
        "{header}이(가) auth.headers와 충돌합니다(대소문자 구분 없음): 자격 증명 헤더는 auth 섹션만 기록할 수 있습니다"
    ),
    "val_ce_header_name_duplicate": (
        "{header}이(가) 같은 맵의 {first}과(와) 대소문자만 다릅니다: HTTP 헤더 이름은 대소문자를 구분하지 않아 "
        "둘 다 전송됩니다"
    ),
    "val_ce_auth_query_conflict": (
        "URL에 이미 auth.query로 선언된 쿼리 파라미터 {param}이(가) 있습니다: "
        "자격 증명 쿼리 파라미터는 auth 섹션만 기록할 수 있습니다"
    ),
    "val_ce_auth_query_reserved": "auth.query 항목 {param}이(가) 아티팩트 다운로드가 이미 사용하는 파라미터와 충돌합니다. 다운로드 시점에 자격 증명이 덮어써지므로 다른 이름을 선택해 주세요",
    "val_ce_task_id_out_of_scope": "task_id는 poll과 result 섹션에서만 사용할 수 있습니다",
    "val_ce_result_id_out_of_scope": "result_id는 result 섹션에서만 사용할 수 있습니다",
    "val_ce_result_id_without_extract": "result_id를 참조하지만 poll.extract가 result_id를 선언하지 않습니다",
    "val_ce_input_out_of_scope": (
        "에셋 {name}은(는) submit에서만 참조할 수 있습니다: poll과 result 요청은 에셋을 실지 않습니다"
    ),
    "val_ce_list_input_requires_each": "{name}은(는) 목록 에셋입니다. 보간하지 말고 $each로 펼쳐 주세요",
    "val_ce_each_in_not_list_input": "$each.in이 선언된 목록 에셋이 아닌 {name}을(를) 가리킵니다",
    "val_ce_each_shape_invalid": (
        "$each는 배열 요소를 펼치는 item, 또는 객체 항목을 펼치는 key와 value를 받습니다. "
        "두 형태는 섞을 수 없습니다"
    ),
    "val_ce_each_position_mismatch": (
        "$each 형태가 위치와 맞지 않습니다: 배열 위치에서 요소를 펼치려면 item을, "
        "객체 위치에서 항목을 펼치려면 key와 value를 사용해 주세요"
    ),
    "val_ce_each_alias_reserved": (
        "{name}은(는) 루프 본문 안의 예약 변수이므로 $each 요소 별칭으로 쓸 수 없습니다"
    ),
    "val_ce_when_unknown_input": "$when이 선언된 에셋이 아닌 {name}을(를) 가리킵니다",
    "val_ce_input_not_referenced": (
        "에셋이 선언되었지만 submit에서 한 번도 참조하지 않습니다: 전송되지 않으며, 기능의 근거도 될 수 없습니다"
    ),
    "val_ce_enum_map_variable_not_allowed": "{variable}은(는) 매핑할 수 없습니다. 매핑 가능한 변수: {allowed}",
    "val_ce_default_variable_not_allowed": "{variable}은(는) 기본값을 둘 수 없습니다. 기본값을 둘 수 있는 변수: {allowed}",
    "val_ce_default_value_type_invalid": "{variable}의 기본값은 {expected} 타입이어야 합니다",
    "val_ce_default_value_not_in_enum_map": "기본값 {value}은(는) enum_maps에 없습니다. {variable}에 사용할 수 있는 값: {allowed}",
    "val_ce_status_map_target_invalid": "상태 {target}은(는) {allowed} 범위를 벗어납니다. 만료 의미는 failed로 매핑해 주세요",
    "val_ce_capability_declared_without_input": (
        "{capability}이(가) 선언되었지만 submit이 {source} 에셋을 참조하지 않습니다. 그러면 이 기능 표시는 거짓이 됩니다"
    ),
    "val_ce_capability_input_without_declaration": (
        "submit이 {source} 에셋을 {capability} 선언 없이 참조합니다. "
        "에셋은 전송되는데 UI는 해당 기능을 숨깁니다"
    ),
    "val_ce_capability_incoherent": "기능 {capability}이(가) 같은 그룹과 충돌합니다. 필요한 조합: {requirement}",
    "val_ce_capability_not_declared": "capabilities에 기능을 최소 하나는 true로 선언해야 합니다: {allowed}",
    "val_ce_media_type_field_not_allowed": "{name}은(는) 미디어 타입이 {media_type}인 정의에서 사용할 수 없습니다",
    "val_ce_artifact_extract_missing": "아티팩트 추출 경로가 없습니다. 다음 중 하나 이상을 작성해야 합니다: {keys}",
    "val_ce_jsonpath_not_a_string": "추출 경로는 문자열이어야 합니다: {path_expression}",
    "val_ce_jsonpath_surrounding_whitespace": "추출 경로 앞뒤에 공백을 둘 수 없습니다: {path_expression}",
    "val_ce_jsonpath_missing_root": "추출 경로는 $로 시작해야 합니다: {path_expression}",
    "val_ce_jsonpath_recursive_descent": (
        "추출 경로에서 재귀 하강은 허용되지 않습니다({position}번째 문자): {path_expression}"
    ),
    "val_ce_jsonpath_union": (
        "추출 경로에서 유니언 선택자는 허용되지 않습니다({position}번째 문자): {path_expression}"
    ),
    "val_ce_jsonpath_slice_step": (
        "추출 경로에서 슬라이스 단계는 허용되지 않습니다({position}번째 문자): {path_expression}"
    ),
    "val_ce_jsonpath_function_extension": (
        "추출 경로에서 함수 확장은 허용되지 않습니다({position}번째 문자): {path_expression}"
    ),
    "val_ce_jsonpath_filter_root_reference": (
        "필터는 루트 노드를 참조할 수 없습니다({position}번째 문자): {path_expression}"
    ),
    "val_ce_jsonpath_filter_non_singular": (
        "필터는 단일 쿼리만 사용할 수 있습니다({position}번째 문자): {path_expression}"
    ),
    "val_ce_jsonpath_regex_operator": (
        "추출 경로에서 정규식 일치 연산자는 허용되지 않습니다({position}번째 문자): {path_expression}"
    ),
    "val_ce_jsonpath_syntax": "추출 경로 구문 오류({position}번째 문자): {path_expression}",
    "val_ce_jsonpath_evaluation_failed": "추출 경로를 평가할 수 없습니다: {path_expression}",
    "val_ce_template_render_failed": "요청 템플릿을 렌더링할 수 없습니다: {detail}",
    "val_ce_auth_literal_credential": (
        "이 값에 실제 시크릿 키가 들어 있는 것 같습니다: api_key 플레이스홀더로 자격 증명을 참조해 주세요. "
        "그러지 않으면 정의를 내보내거나 공유할 때 키가 노출됩니다"
    ),
    "val_ce_template_url_not_string": "URL 템플릿은 문자열로 렌더링되어야 합니다",
    "val_ce_unknown_asset_encoding": "알 수 없는 에셋 인코딩입니다: {encoding}",
    "val_ce_enum_map_value_missing": "enum_maps.{name}에 '{value}' 항목이 없습니다",
    "val_ce_template_text_variable_null": "변수 {name}이(가) null이어서 텍스트에 넣을 수 없습니다",
    "val_ce_each_value_not_list": "$each.in이 가리키는 {name}의 런타임 값이 목록이 아닙니다",
    # ---- ComfyUI endpoint: node bindings and import routing ----
    "val_ce_comfyui_binding_required": (
        "이 엔드포인트를 저장하려면 {binding_key}을(를) 노드에 바인딩해야 합니다: "
        "prompt가 무엇을 그릴지 정하고, output이 어떤 파일을 가져올지 정합니다"
    ),
    "val_ce_comfyui_binding_key_not_allowed": (
        "{media_type} 엔드포인트에는 {binding_key} 바인딩이 없습니다. 사용 가능한 키: {allowed}"
    ),
    "val_ce_comfyui_node_not_found": (
        "워크플로에 노드 {node}이(가) 없습니다: 노드 id는 워크플로를 편집할 때마다 바뀌므로, "
        "워크플로를 다시 가져온 뒤 노드 바인딩을 확인해 주세요"
    ),
    "val_ce_comfyui_input_not_found": "노드 {node}에 {input}이라는 입력이 없습니다",
    "val_ce_comfyui_input_is_link": (
        "입력 {input}은(는) 노드 {node}에서 상위 노드가 와이어로 연결해 놓은 자리라 실행 시점에 덮어써집니다. "
        "대신 리터럴 필드를 바인딩해 주세요"
    ),
    "val_ce_comfyui_target_collision": (
        "입력 {input}은(는) 노드 {node}에서 이미 {owner}이(가) 기록하는 자리라, {binding_key}이(가) 같은 필드에 쓸 수 없습니다: "
        "나중에 채워지는 쪽이 다른 쪽을 덮어씁니다"
    ),
    "val_ce_comfyui_class_type_mismatch": (
        "항목에는 노드 {node}이(가) {class_type}(으)로 기록되어 있는데, 워크플로에는 이제 {actual}(으)로 되어 있습니다: "
        "재매칭은 노드를 타입으로 식별하므로 불일치가 있으면 바인딩이 다른 곳으로 옮겨갑니다. "
        "다시 가져온 뒤 바인딩을 확인해 주세요"
    ),
    "val_ce_comfyui_consumer_not_fed": (
        "참조 이미지 노드 {node}에서 나온 흐름은 입력 {input}이(가) 있는 노드 {consumer}까지 닿지 않습니다: "
        "소비 노드 기록이 틀리면 이미지 수가 더 적은 요청이 상관없는 입력을 다시 연결해 버립니다"
    ),
    "val_ce_comfyui_fps_conflict": (
        "프레임 레이트의 출처가 여럿이고 서로 충돌합니다({values}): 길이를 프레임 수로 바꾸려면 "
        "프레임 레이트가 정확히 하나여야 하니, 그중 하나만 남겨 주세요"
    ),
    "val_ce_comfyui_ui_format_workflow": (
        "이것은 ComfyUI UI 형식 워크플로라 제출할 수 없습니다. 대신 ComfyUI에서 Export (API)로 내보내 주세요"
    ),
    # ---- ComfyUI endpoint: node binding inference signals and hints ----
    "val_ce_infer_manual_binding": "저장된 노드 바인딩입니다. 사용자가 이미 확인한 대상은 그대로 유지합니다",
    "val_ce_infer_title_marker": "노드 제목에 ARCREEL: 마커가 있습니다",
    "val_ce_infer_external_node_family": "{family} 파라미터 노드가 파라미터 {parameter}을(를) 선언합니다",
    "val_ce_infer_sampler_port_trace": "{port} 컨디셔닝 포트(노드 {node})에서 거슬러 올라가 추적했습니다",
    "val_ce_infer_alias_with_class_type": "{class_type}이(가) 흔히 이 의미를 담당합니다",
    "val_ce_infer_alias_only": "입력 이름 {input}은(는) 이 의미의 흔한 이름입니다",
    "val_ce_infer_link_trace": "그 출력이 입력 {input}을(를) 통해 노드 {consumer}에 공급됩니다",
    "val_ce_infer_class_type_tier": "{class_type}은(는) 후보 중에서 더 신뢰할 수 있는 타입입니다",
    "val_ce_infer_output_chain": "최종 출력을 만드는 체인 위에 놓여 있습니다",
    "val_ce_infer_title_polarity": "노드 제목 \"{title}\"이(가) 이 극성을 가리킵니다",
    "val_ce_infer_note_reference_consumer_unknown": (
        "참조 이미지는 입력 {input}이(가) 속한 노드 {node}({class_type})에 공급됩니다. 이 입력은 이미지 수가 줄어들 때 "
        "다시 연결할 수 없으므로, 남은 자리는 마지막 이미지를 반복해 채웁니다"
    ),
    "val_ce_infer_note_batch_size_above_one": (
        "입력 {input}이(가) 속한 노드 {node}({class_type})의 입력 값이 {value}이므로 한 번 제출로 여러 이미지가 나옵니다. "
        "ArcReel은 이 값을 바꾸지 않습니다"
    ),
    "val_ce_infer_note_manual_only_node": (
        "노드 {node}은(는) {class_type}입니다. 이 노드가 가진 {binding_keys}은(는) 추론할 수 없으니 직접 바인딩해 주세요"
    ),
    "val_ce_infer_note_computed_source": (
        "{binding_key} 후보는 입력 {input}이(가) 속한 노드 {node}에 닿지만, 그 값은 상위에서 계산되어 기록할 수 없습니다. 직접 지정해 주세요"
    ),
    "val_ce_infer_note_rematched": "{binding_key} 항목을 노드 {nodes}에 재매칭했습니다",
    "val_ce_infer_note_binding_lost": (
        "{binding_key} 항목은 새 워크플로에 대상이 없습니다(이전에는 노드 {nodes}). "
        "추론을 다시 실행했으니 확인해 주세요"
    ),
    "val_ce_infer_note_target_taken": (
        "{binding_key} 후보는 입력 {input}이(가) 속한 노드 {node}에 닿지만, {others}도(도) 그곳에 기록합니다. "
        "한 필드에는 바인딩을 하나만 둘 수 있어 {binding_key} 후보에서 제외했습니다"
    ),
    "val_ce_poll_without_task_id": "폴링 요청이 task_id를 전혀 참조하지 않습니다. 의도한 것인지 확인해 주세요",
    "val_ce_jsonpath_wildcard_order": (
        "{path_expression}은(는) 와일드카드를 사용합니다: 객체 와일드카드는 첫 멤버만 가져오며, "
        "키 순서는 미리보기와 백엔드 사이에서 다를 수 있습니다"
    ),
    # ---- market source checks ----
    "val_market_index_unreadable": "인덱스 파일을 읽을 수 없습니다: {detail}",
    "val_market_unsupported_schema_version": "인덱스의 schema_version {version}은(는) 지원하는 {supported}보다 새로운 버전입니다",
    "val_market_missing_field": "필수 필드가 누락되었습니다: {field}",
    "val_market_invalid_type": "타입이 올바르지 않습니다. {expected} 타입이어야 합니다",
    "val_market_invalid_value": "값이 제약 {keyword}을(를) 위반합니다: {constraint}",
    "val_market_slug_invalid": (
        '슬러그 "{value}"이(가) 올바르지 않습니다: 소문자, 숫자, 하이픈만 사용하고, '
        "문자 또는 숫자로 시작해야 하며, 최대 64자입니다"
    ),
    "val_market_slug_duplicate": '슬러그 "{slug}"이(가) 이 마켓 소스에서 두 번 이상 사용됩니다',
    "val_market_slug_directory_mismatch": '슬러그 "{slug}"이(가) 정의 디렉터리 "{directory}"과(와) 일치하지 않습니다',
    "val_market_path_not_relative": (
        '"{value}"은(는) 마켓 소스 안의 상대 경로여야 합니다: '
        "앞의 /나 스킴을 쓸 수 없고, ..도 안 되며, 소스 밖을 가리켜서는 안 됩니다"
    ),
    "val_market_file_missing": "참조된 파일이 존재하지 않습니다: {value}",
    "val_market_symlink_not_allowed": (
        '"{value}"은(는) 심볼릭 링크입니다. GitHub raw로 가져오는 클라이언트는 링크 대상 경로 텍스트를 받게 되니, '
        "일반 파일이나 디렉터리를 사용해 주세요"
    ),
    "val_market_icon_format_invalid": "아이콘은 내용과 확장자가 일치하는, 읽을 수 있는 PNG, WebP 또는 SVG여야 합니다",
    "val_market_icon_too_large": "아이콘이 {size}바이트로 {limit}바이트 제한을 초과합니다",
    "val_market_icon_not_square": "아이콘은 정사각형이어야 합니다. 현재 {width}×{height}입니다",
    "val_market_icon_ambiguous": "항목 디렉터리에는 아이콘 파일을 하나만 둘 수 있습니다. 발견된 파일: {icons}",
    "val_market_definition_unreadable": "정의를 읽을 수 없습니다: {detail}",
    "val_market_definition_invalid": "정의가 검증에 실패했습니다({code}): {detail}",
    "val_market_projection_mismatch": (
        '인덱스 필드 {field}의 값이 "{index_value}"인데, 정의 meta의 "{definition_value}"과(와) 다릅니다'
    ),
    "val_market_min_app_version_invalid": 'min_app_version "{value}"이(가) semver (x.y.z) 형식이 아닙니다',
    "val_market_detail_meta_not_object": "정의에 meta 객체가 없습니다",
    "val_market_cli_check_passed": "마켓 소스 검사를 통과했습니다: {directory}",
    "val_market_cli_check_failed": "마켓 소스 검사에서 {count}개 문제가 나왔습니다",
    "val_market_cli_generate_written": "{path}에 기록했습니다 ({count}개 항목)",
    "val_market_cli_generate_failed": "인덱스를 생성할 수 없습니다: {count}개 문제",
}
