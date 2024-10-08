/*
 *  Copyright (c) 2024 hikyuu.org
 *
 *  Created on: 2024-05-27
 *      Author: fasiondog
 */

#pragma once

#include "OperatorValueSelector.h"

namespace hku {

class HKU_API OperatorAddValueSelector : public OperatorValueSelector {
    OPERATOR_VALUE_SELECTOR_IMP(OperatorAddValueSelector, "SE_AddValue")
    OPERATOR_VALUE_SELECTOR_SERIALIZATION
};

}  // namespace hku