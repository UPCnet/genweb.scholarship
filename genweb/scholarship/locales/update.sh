#! /bin/bash

domain=genweb.scholarship

export PATH=../../../../../bin

i18ndude rebuild-pot --pot $domain.pot --create $domain ../
i18ndude sync --pot $domain.pot */LC_MESSAGES/$domain.po

msgfmt -o ca/LC_MESSAGES/$domain.mo  ca/LC_MESSAGES/$domain.po
msgfmt -o es/LC_MESSAGES/$domain.mo  es/LC_MESSAGES/$domain.po
msgfmt -o en/LC_MESSAGES/$domain.mo  en/LC_MESSAGES/$domain.po
