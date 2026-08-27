# Product and Production Writing

## UX principle

Name the user's action or state. Do not narrate the interface unless interaction is genuinely unclear.

❌ `اضغط على الزر أدناه للمتابعة.`

✅ `متابعة`

## Success

❌ `تم حفظ التغييرات بنجاح.`

Possible:

✅ `حُفظت التغييرات.`

✅ `حفظنا التغييرات.`

✅ `تغييراتك محفوظة.`

Choose according to product voice. Do not make `تم` a universal ban.

## Errors

Say what happened and how to recover.

❌ `حدث خطأ غير معروف.`

✅ `تعذّر الحفظ. حاول مرة أخرى.`

## Destructive actions

State consequence explicitly.

Title:
`حذف الحساب؟`

Body:
`سيُحذف حسابك وبياناتك نهائيًا. لا يمكن التراجع.`

Action:
`حذف الحساب`

## Placeholders and tokens

Preserve exactly unless the task explicitly changes them:

- `{name}`
- `{count}`
- `%s`
- `%d`
- `{{userName}}`
- tags
- URLs
- emails
- filenames
- product names
- codes

Move surrounding Arabic if needed, not the token.

## Arabic plurals

Do not reuse English singular/plural logic.

Typical forms:

- `لا توجد رسائل`
- `رسالة واحدة`
- `رسالتان`
- `3 رسائل`
- `11 رسالة`

Use the actual i18n system when dynamic counts are implemented.

## RTL and mixed text

Arabic is RTL; emails, codes, URLs, and many product names are LTR.

Keep mixed strings short and test them visually.

Examples:

`أرسلنا الرمز إلى name@example.com`

`استخدم الرمز SAVE20 عند الدفع`

## Numerals and currency

Follow existing product convention. Do not “correct” numeral style without a reason.

Examples:

`29 ريالًا شهريًا`

`29 ر.س`

## Product terminology

Prefer one term per concept. Consistency is part of naturalness.
