#ifndef MYADAPTATIONMANAGER_H
#define MYADAPTATIONMANAGER_H

#include "BaseAdaptationManager.h"
#include "MyAdaptationManager.h"
#include "managers/adaptation/UtilityScorer.h"
#include "managers/execution/AllTactics.h"



class MyAdaptationManager : public BaseAdaptationManager {
public:
    virtual Tactic* evaluate() override;
};
Define_Module(MyAdaptationManager)
#endif // MYADAPTATIONMANAGER_H