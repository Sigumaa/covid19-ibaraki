<template>
  <div>
    <card-row class="DataBlock">
      <!-- 新規患者に関する報告件数の推移 -->
      <confirmed-cases-number-card />
      <!-- 週単位の陽性者増加比 -->
      <confirmed-cases-increase-ratio-by-week-card />
      <!-- 経路不明者 -->
      <untracked-rate-card />
      <!-- 陽性患者の属性 -->
      <confirmed-cases-attributes-card />
      <!-- 回復者数 -->
      <recovered-card />
      <!-- 死亡者数 -->
      <deaths-card />
      <!-- 市町村別患者数 -->
      <ibaraki-city-map-card />
      <!-- 年代別患者数 -->
      <confirmed-cases-by-age />
      <!-- 検査陽性率 -->
      <positive-rate-card />
      <!-- 検査実施人数（県） -->
      <inspection-persons-number-card />
      <!-- 新型コロナコールセンター相談件数 -->
      <telephone-advisory-reports-number-card />
    </card-row>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import CardRow from '@/components/cards/CardRow.vue'
import ConfirmedCasesNumberCard from '@/components/wave3/ConfirmedCasesNumberCard.vue'
import ConfirmedCasesAttributesCard from '@/components/wave3/ConfirmedCasesAttributesCard.vue'
import IbarakiCityMapCard from '@/components/wave3/IbarakiCityMapCard.vue'
import InspectionPersonsNumberCard from '@/components/wave3/InspectionPersonsNumberCard.vue'
import TelephoneAdvisoryReportsNumberCard from '@/components/wave3/TelephoneAdvisoryReportsNumberCard.vue'
import RecoveredCard from '@/components/wave3/RecoveredCard.vue'
import DeathsCard from '@/components/wave3/DeathsCard.vue'
import PositiveRateCard from '@/components/wave3/PositiveRateCard.vue'
import ConfirmedCasesIncreaseRatioByWeekCard from '@/components/wave3/ConfirmedCasesIncreaseRatioByWeekCard.vue'
import ConfirmedCasesByAge from '@/components/wave3/ConfirmedCasesByAge.vue'
import UntrackedRateCard from '@/components/wave3/UntrackedRateCard.vue'

export default Vue.extend({
  components: {
    CardRow,
    ConfirmedCasesNumberCard,
    ConfirmedCasesAttributesCard,
    IbarakiCityMapCard,
    InspectionPersonsNumberCard,
    TelephoneAdvisoryReportsNumberCard,
    RecoveredCard,
    DeathsCard,
    PositiveRateCard,
    ConfirmedCasesIncreaseRatioByWeekCard,
    ConfirmedCasesByAge,
    UntrackedRateCard,
  },
})
</script>

<style lang="scss" scoped>
.DataBlock {
  margin: 20px -8px;

  .DataCard {
    @include largerThan($medium) {
      padding: 10px;
    }

    @include lessThan($small) {
      padding: 4px 8px;
    }
  }
}
</style>
