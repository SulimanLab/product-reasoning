# Golden Cases

Use these cases to evaluate whether a model learned the method rather than memorized a blacklist.

## Case 1 — direct verb

Input:
`قم بالضغط على زر المتابعة من أجل الانتقال إلى الخطوة التالية.`

Expected:
`متابعة`

Acceptable if explicit instruction is needed:
`تابع إلى الخطوة التالية.`

Reject: keeping `قم بـ` or unnecessary UI narration.

## Case 2 — semantic metaphor

Input:
`ما الذي يبدو عليه القلق بالنسبة لك؟`

Expected:
`كيف يظهر القلق عندك؟`

Reject: cosmetic edits that preserve the imported frame.

## Case 3 — no purism

Input:
`التطبيق يدعم الوضع الداكن.`

Expected:
Usually leave unchanged.

Reject: changing `يدعم` solely because it may be a modern semantic extension.

## Case 4 — context-dependent rewrite

Input:
`نحن هنا لمساعدتك على فهم الأنماط التي قد تؤثر على نومك.`

Expected:
Inspect the surface.

Heading:
`ما الذي يؤثر على نومك؟`

Body:
`نفهم معًا ما الذي قد يؤثر على نومك.`

Reject: declaring the original ungrammatical or universally forbidden.

## Case 5 — leave natural Arabic

Input:
`لا توجد مواعيد متاحة اليوم.`

Expected:
Leave unchanged.

Reject:
`ليس ثمة مواعيد متاحة لهذا اليوم.`

## Case 6 — success residue

Input:
`لقد قمت بإكمال التمرين بنجاح.`

Expected:
`أكملت التمرين.`

## Case 7 — translated slogan

Input:
`ابدأ رحلتك لتصبح أفضل نسخة من نفسك.`

Expected:
Rewrite the concrete promise from meaning.

Possible:
`ابدأ بخطوة تساعدك على فهم نفسك أكثر.`

Reject: swapping one word while preserving the slogan frame.

## Case 8 — source English

Input:
`Your session is confirmed.`

Possible:
`موعد جلستك مؤكد.`
`أكدنا موعد جلستك.`

Choice depends on voice.

## Case 9 — source English interaction

Input:
`Take a moment to check in with yourself.`

Weak:
`خذ لحظة للتحقق من نفسك.`

Possible:
`توقف قليلًا ولاحظ كيف تشعر.`

Interactive surface:
`كيف تشعر الآن؟`

## Case 10 — local natural term

Input:
`أدخل رقم جوالك.`

Expected:
Leave unchanged in a Saudi consumer product using `جوال`.

Reject:
`أدخل رقم هاتفك المحمول.` merely to sound formal.

## Case 11 — conditional distinction

Input:
`عندما تحتاج إلى مساعدة، تواصل معنا.`

Expected:
`إذا احتجت إلى مساعدة، تواصل معنا.`

But do not generalize to all `عندما`.

## Case 12 — preposition relation

Input:
`يمكنك تحديث الملف من خلال صفحة الإعدادات.`

Expected:
`يمكنك تحديث الملف من صفحة الإعدادات.`

or a better context-specific structure.
