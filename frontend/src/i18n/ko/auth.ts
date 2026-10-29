import type enAuth from "@/i18n/en/auth";

export default {
  'login': '로그인',
  'logging_in': '로그인 중...',
  'login_failed': '로그인 실패',
  'username': '사용자 이름',
  'password': '비밀번호',
  'login_subtitle': '계정으로 로그인하세요',
} satisfies Record<keyof typeof enAuth, string>;
