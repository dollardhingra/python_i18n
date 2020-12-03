import gettext

t = gettext.translation("python_i18n", localedir="locale", languages=["hi_IN"])

_ = t.gettext

greeting = _("Hello, world!")
