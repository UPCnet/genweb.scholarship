#! /bin/bash

domain=genweb.scholarship

export PATH=../../../../../bin

i18ndude rebuild-pot --pot $domain.pot --create $domain ../
i18ndude sync --pot $domain.pot */LC_MESSAGES/$domain.po
