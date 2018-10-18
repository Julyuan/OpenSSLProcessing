/*
 * Copyright 2000-2016 The OpenSSL Project Authors. All Rights Reserved.
 *
 * Licensed under the OpenSSL license (the "License").  You may not use
 * this file except in compliance with the License.  You can obtain a copy
 * in the file LICENSE in the source distribution or at
 * https://www.openssl.org/source/license.html
 */

#include <stdio.h>
#include "../include/cryptlib.h"
#include "../include/asn1.h"
#include "../include/asn1t.h"
#include "../include/cms.h"
#include "../include/dh.h"
#include "../include/ocsp.h"
#include "../include/pkcs7.h"
#include "../include/pkcs12.h"
#include "../include/rsa.h"
#include "../include/x509v3.h"

#include "asn1_item_list.h"

const ASN1_ITEM *ASN1_ITEM_lookup(const char *name)
{
    size_t i;

    for (i = 0; i < OSSL_NELEM(asn1_item_list); i++) {
        const ASN1_ITEM *it = ASN1_ITEM_ptr(asn1_item_list[i]);

        if (strcmp(it->sname, name) == 0)
            return it;
    }
    return NULL;
}

const ASN1_ITEM *ASN1_ITEM_get(size_t i)
{
    if (i >= OSSL_NELEM(asn1_item_list))
        return NULL;
    return ASN1_ITEM_ptr(asn1_item_list[i]);
}
