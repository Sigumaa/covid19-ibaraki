<template>
  <v-col cols="12" md="6" class="DataCard">
    <data-view
      :title="$t('市町村毎の感染状況（地図）')"
      :title-id="'ibaraki-city-map-table'"
      :date="Data.patients.date"
    >
      <template v-slot:button>
        <p :class="$style.note">
          {{ $t('・回復している人数を含む') }}<br />
          {{ $t('・人口1万人あたりの感染者数（人口は2020年8月現在のもの）') }}
        </p>
        <p :class="$style.note2">{{ $t('凡例（単位は人）') }}</p>
        <table :class="$style.note2">
          <tbody>
            <tr>
              <td><span class="color-test infected-level1" />1.5未満</td>
              <td><span class="color-test infected-level2" />1.5 - 3.0</td>
              <td><span class="color-test infected-level3" />3.0 - 4.5</td>
            </tr>
            <tr>
              <td><span class="color-test infected-level4" />4.5 - 6.0</td>
              <td><span class="color-test infected-level5" />6.0 - 7.5</td>
              <td><span class="color-test infected-level6" />7.5以上</td>
            </tr>
          </tbody>
        </table>
      </template>
      <ibaraki-map />
    </data-view>
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import IbarakiMap from '@/assets/ibaraki-map.svg'
import DataView from '@/components/DataView.vue'
import CityData from '@/data/cities.json'

export default {
  components: {
    IbarakiMap,
    DataView,
  },
  data() {
    return {
      Data,
    }
  },
  mounted() {
    const patients = Data.patients.data
    // 市町村の患者人数の連想配列
    const cityPatientsNumber = {}
    const cityPatientsRate = {}
    for (const key of patients) {
      cityPatientsNumber[key.居住地] = patients.filter(function (x) {
        return x.居住地 === key.居住地
      }).length
    }

    CityData.forEach((element) => {
      if (!cityPatientsNumber[element.city]) {
        return
      }

      cityPatientsRate[element.city] =
        (cityPatientsNumber[element.city] / element.population) * 10000

      const targetElement = document.getElementById(
        'ibaraki-map_svg__' + element.Romaji
      )
      if (cityPatientsRate[element.city] < 1.5)
        targetElement.classList.add('infected-level1')
      else if (cityPatientsRate[element.city] < 3.0)
        targetElement.classList.add('infected-level2')
      else if (cityPatientsRate[element.city] < 4.5)
        targetElement.classList.add('infected-level3')
      else if (cityPatientsRate[element.city] < 6.0)
        targetElement.classList.add('infected-level4')
      else if (cityPatientsRate[element.city] < 7.5)
        targetElement.classList.add('infected-level5')
      else targetElement.classList.add('infected-level6')
    })
  },
}
</script>

<style lang="scss" module>
.note {
  @include font-size(12);

  margin-top: 10px;
  margin-bottom: 0;
  color: $gray-3;

  &2 {
    @include font-size(14);

    td {
      padding-left: 16px;
    }
  }
}
</style>
<!-- 本来ならばSVGをinline展開してそこに限定してcssを適用するべきだが、inline展開ができなかったため妥協 -->
<style lang="scss">
$infected-level1: #ccfbcc;
$infected-level2: #88f2a9;
$infected-level3: #44e5b7;
$infected-level4: #00c1d5;
$infected-level5: #004da5;
$infected-level6: #000072;

.color-test {
  display: inline-block;
  width: 2.5rem;
  height: 1rem;
  margin: 0 0.5rem 0 0;
  vertical-align: middle;
}
// 1-5

.infected-level1 {
  background-color: $infected-level1;
  fill: $infected-level1 !important;
}
// 6-10

.infected-level2 {
  background-color: $infected-level2;
  fill: $infected-level2 !important;
}
// 10-15

.infected-level3 {
  background-color: $infected-level3;
  fill: $infected-level3 !important;
}
// 15-20

.infected-level4 {
  background-color: $infected-level4;
  fill: $infected-level4 !important;
}
// 21-30

.infected-level5 {
  background-color: $infected-level5;
  fill: $infected-level5 !important;
}
// 31-

.infected-level6 {
  background-color: $infected-level6;
  fill: $infected-level6 !important;
}

svg {
  max-height: 600px;
}
</style>
