/*
 *  Copyright (c) 2024 hikyuu.org
 *
 *  Created on: 2024-08-25
 *      Author: fasiondog
 */

#pragma once

#include "hikyuu/trade_sys/portfolio/Portfolio.h"
#include "Strategy.h"

namespace hku {

class HKU_API RunPortfolioInStrategy {
public:
    RunPortfolioInStrategy() = default;
    RunPortfolioInStrategy(const PFPtr& pf, const KQuery& query, int adjust_cycle,
                           const OrderBrokerPtr& broker, const TradeCostPtr& costfunc);
    virtual ~RunPortfolioInStrategy() = default;

    void run();

private:
    PFPtr m_pf;
    OrderBrokerPtr m_broker;
    KQuery m_query;
    int m_adjust_cycle = 1;
};

StrategyPtr HKU_API crtPFStrategy(const PFPtr& pf, const KQuery& query, int adjust_cycle,
                                  const OrderBrokerPtr& broker, const TradeCostPtr& costfunc,
                                  const string& name = "PFStrategy",
                                  const std::vector<OrderBrokerPtr>& other_brokers = {},
                                  const string& config_file = "");

}  // namespace hku