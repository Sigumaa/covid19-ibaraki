<template>
  <v-col cols="12" md="6" class="DataCard">
    <data-view
      :title="$t('茨城版コロナNext')"
      :title-id="'ibaraki-corona-next'"
      :date="Data.ibk_corona_next.date"
    >
      <template v-slot:button>
        <ul :class="$style.note">
          <li>{{ $t('各値は直近1週間の平均値') }}</li>
        </ul>
        <ul :class="$style.container">
          <li style="width: 100%; list-style: none;">
            <div
              :class="$style.content"
              style="display: block; min-height: fit-content;"
            >
              <span>
                {{ $t('現在の対策状況：') }}
                <span :class="$style.unit">Stage</span>
                <strong>{{ Data.ibk_corona_next.stage }}</strong>
              </span>
            </div>
          </li>
        </ul>
        <table class="ibkCoronaNext">
          <thead>
            <tr>
              <th colspan="2" style="background-color: #d9d9d9;">
                {{ $t('県内の医療提供体制') }}
              </th>
              <th colspan="1" style="background-color: #98d6a4;">
                {{ $t('都内の感染状況') }}
              </th>
            </tr>
            <tr>
              <th>{{ $t('重症病床稼働率') }}</th>
              <th>{{ $t('病床稼働率') }}</th>
              <th>{{ $t('1日当たりの経路不明陽性者数') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <strong>{{ patients.pillar.toFixed(1) }}</strong>
                <span :class="$style.unit">%</span>
              </td>
              <td>
                <strong>{{ patients.sickbed.toFixed(1) }}</strong>
                <span :class="$style.unit">%</span>
              </td>
              <td>
                <strong>{{ avg.tokyo.toFixed(1) }}</strong>
                <span :class="$style.unit">{{ $t('人') }}</span>
              </td>
            </tr>
            <tr>
              <td>
                <span
                  :class="['stageMark', 'MarkSmall', `stage${stage.pillar}`]"
                />
                <span :class="$style.unit">Stage</span>
                <strong>{{ stage.pillar.toLocaleString() }}</strong>
              </td>
              <td>
                <span
                  :class="['stageMark', 'MarkSmall', `stage${stage.sickbed}`]"
                />
                <span :class="$style.unit">Stage</span>
                <strong>{{ stage.sickbed.toLocaleString() }}</strong>
              </td>
              <td>
                <span
                  :class="['stageMark', 'MarkSmall', `stage${stage.tokyo}`]"
                />
                <span :class="$style.unit">Stage</span>
                <strong>{{ stage.tokyo.toLocaleString() }}</strong>
              </td>
            </tr>
            <tr :class="$style.additionalData">
              <td>
                <span :class="$style.delta">{{ $t('前日比') }}:&nbsp;</span>
                <strong>{{ deltaStr.pillar }}</strong>
                <span :class="$style.unit">%</span>
              </td>
              <td>
                <span :class="$style.delta">{{ $t('前日比') }}:&nbsp;</span>
                <strong>{{ deltaStr.sickbed }}</strong>
                <span :class="$style.unit">%</span>
              </td>
              <td>
                <span :class="$style.delta">{{ $t('前日比') }}:&nbsp;</span>
                <strong>{{ deltaStr.tokyo }}</strong>
                <span :class="$style.unit">{{ $t('人') }}</span>
              </td>
            </tr>
            <tr :class="$style.additionalData">
              <td>
                <span :class="$style.delta" />
                <strong>{{ updDate.pillar }}</strong>
                <span :class="$style.unit"> 時点</span>
              </td>
              <td>
                <span :class="$style.delta" />
                <strong>{{ updDate.sickbed }}</strong>
                <span :class="$style.unit"> 時点</span>
              </td>
              <td>
                <span :class="$style.delta" />
                <strong>{{ updDate.tokyo }}</strong>
                <span :class="$style.unit"> 時点</span>
              </td>
            </tr>
          </tbody>
        </table>
        <table class="ibkCoronaNext">
          <thead>
            <tr>
              <th colspan="3" style="background-color: #99a8e0;">
                {{ $t('県内の感染状況') }}
              </th>
            </tr>
            <tr>
              <th>{{ $t('1日当たりの陽性者数') }}</th>
              <th>{{ $t('陽性者のうち濃厚接触者以外の数') }}</th>
              <th>{{ $t('陽性率') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <strong>{{ avg.new_patients.toFixed(1) }}</strong>
                <span :class="$style.unit">{{ $t('人') }}</span>
              </td>
              <td>
                <strong>{{ avg.non_closecontact.toFixed(1) }}</strong>
                <span :class="$style.unit">{{ $t('人') }}</span>
              </td>
              <td>
                <strong>{{ patients.rate.toFixed(1) }}</strong>
                <span :class="$style.unit">%</span>
              </td>
            </tr>
            <tr>
              <td>
                <span
                  :class="[
                    'stageMark',
                    'MarkSmall',
                    `stage${stage.new_patients}`,
                  ]"
                />
                <span :class="$style.unit">Stage</span>
                <strong>{{ stage.new_patients.toLocaleString() }}</strong>
              </td>
              <td>
                <span
                  :class="[
                    'stageMark',
                    'MarkSmall',
                    `stage${stage.non_closecontact}`,
                  ]"
                />
                <span :class="$style.unit">Stage</span>
                <strong>{{ stage.non_closecontact.toLocaleString() }}</strong>
              </td>
              <td>
                <span
                  :class="['stageMark', 'MarkSmall', `stage${stage.rate}`]"
                />
                <span :class="$style.unit">Stage</span>
                <strong>{{ stage.rate.toLocaleString() }}</strong>
              </td>
            </tr>
            <tr :class="$style.additionalData">
              <td>
                <span :class="$style.delta">{{ $t('前日比') }}:&nbsp;</span>
                <strong>{{ deltaStr.new_patients }}</strong>
                <span :class="$style.unit">{{ $t('人') }}</span>
              </td>
              <td>
                <span :class="$style.delta">{{ $t('前日比') }}:&nbsp;</span>
                <strong>{{ deltaStr.non_closecontact }}</strong>
                <span :class="$style.unit">{{ $t('人') }}</span>
              </td>
              <td>
                <span :class="$style.delta">{{ $t('前日比') }}:&nbsp;</span>
                <strong>{{ deltaStr.rate }}</strong>
                <span :class="$style.unit">%</span>
              </td>
            </tr>
            <tr :class="$style.additionalData">
              <td>
                <span :class="$style.delta" />
                <strong>{{ updDate.new_patients }}</strong>
                <span :class="$style.unit"> 時点</span>
              </td>
              <td>
                <span :class="$style.delta" />
                <strong>{{ updDate.non_closecontact }}</strong>
                <span :class="$style.unit"> 時点</span>
              </td>
              <td>
                <span :class="$style.delta" />
                <strong>{{ updDate.rate }}</strong>
                <span :class="$style.unit"> 時点</span>
              </td>
            </tr>
          </tbody>
        </table>
        <br />
        <p :class="$style.note">
          {{ $t('（参考）茨城版コロナNextにおけるStage指標') }}
        </p>
        <table class="stageTable ibkCoronaNext">
          <tbody>
            <tr>
              <td><span class="stageMark stage1" /></td>
              <td>Stage 1</td>
              <td>{{ $t('感染を抑制できている状態') }}</td>
            </tr>
            <tr>
              <td><span class="stageMark stage2" /></td>
              <td>Stage 2</td>
              <td>{{ $t('感染を概ね抑制できている状態') }}</td>
            </tr>
            <tr>
              <td><span class="stageMark stage3" /></td>
              <td>Stage 3</td>
              <td>{{ $t('感染が拡大している状態') }}</td>
            </tr>
            <tr>
              <td><span class="stageMark stage4" /></td>
              <td>Stage 4</td>
              <td>{{ $t('感染爆発・医療崩壊のリスクが高い状態') }}</td>
            </tr>
          </tbody>
        </table>
      </template>
    </data-view>
  </v-col>
</template>

<script>
import Data from '@/data/data.json'
import DataView from '@/components/DataView.vue'

export default {
  components: {
    DataView,
  },
  data() {
    const patients = Data.ibk_corona_next
    const avgYesterday = {
      new_patients: 0,
      non_closecontact: 0,
      tokyo: 0,
    }
    const avg = { new_patients: 0, non_closecontact: 0, tokyo: 0 }
    const stage = {
      pillar: 1,
      sickbed: 1,
      new_patients: 1,
      non_closecontact: 1,
      rate: 1,
      tokyo: 1,
    }

    avgYesterday.new_patients = patients.new_patients
      .slice(0, -1)
      .reduce((a, b) => a + b.value, 0)
    avgYesterday.non_closecontact = patients.non_closecontact
      .slice(0, -1)
      .reduce((a, b) => a + b.value, 0)
    avgYesterday.tokyo = patients.tokyo
      .slice(0, -1)
      .reduce((a, b) => a + b.value, 0)

    avg.new_patients = patients.new_patients
      .slice(1)
      .reduce((a, b) => a + b.value, 0)
    avg.non_closecontact = patients.non_closecontact
      .slice(1)
      .reduce((a, b) => a + b.value, 0)
    avg.tokyo = patients.tokyo.slice(1).reduce((a, b) => a + b.value, 0)

    for (const key in avg) {
      avgYesterday[key] /= 7
      avg[key] /= 7
    }

    const _ = {
      pillar: patients.pillar,
      sickbed: patients.sickbed,
      rate: patients.rate,
    }
    const _Y = {
      pillar: patients.pillarYesterday,
      sickbed: patients.sickbedYesterday,
      rate: patients.rateYesterday,
    }
    for (const i in avg) {
      _[i] = avg[i]
    }
    for (const i in avgYesterday) {
      _Y[i] = avgYesterday[i]
    }

    const delta = {}
    for (const key in _) {
      delta[key] = _[key] - _Y[key]
    }
    // [ _でのKey, Stage1->2の境値, Stage2->3, Stage3->4]
    const list = [
      ['pillar', 10, 30, 60],
      ['sickbed', 30, 45, 70],
      ['new_patients', 1, 5, 10],
      ['non_closecontact', 1, 3, 5],
      ['rate', 1, 3, 7],
      ['tokyo', 10, 50, 100],
    ]

    for (const l of list) {
      const d = _[l[0]] // Key
      stage[l[0]] += (d > l[1]) + (d > l[2]) + (d > l[3])
    }

    const formatDelta = (n) => {
      let str = ''
      switch (Math.sign(n)) {
        case 1:
          str = '+'
          break
        case -1:
          str = '-'
          break
        case 0:
          str = '±'
          break
      }
      str += ' '
      str += Math.abs(n).toFixed(1)
      return str
    }

    const deltaStr = {}
    for (const key in delta) {
      deltaStr[key] = formatDelta(delta[key])
    }

    const updDate = {
      pillar: patients.date,
      sickbed: patients.date,
      new_patients: patients.new_patients[7].date,
      non_closecontact: patients.non_closecontact[7].date,
      rate: patients.date,
      tokyo: patients.tokyo[7].date,
    }

    for (const key in updDate) {
      const t = new Date(updDate[key])
      updDate[key] = `${String((t.getMonth() + 1) / 10).replace(
        '.',
        ''
      )}/${String(t.getDate() / 10).replace('.', '')}`
    }

    return {
      Data,
      patients,
      avg,
      stage,
      deltaStr,
      updDate,
    }
  },
}
</script>

<style lang="scss" module>
.note {
  @include font-size(12);

  margin-top: 10px;
  margin-bottom: 0;
  color: $gray-3;
}

$default-bdw: 3px;
$default-boxh: 150px;
$default-boxdiff: 35px;

.container {
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  width: 100%;
  // override default styles
  padding-left: 0 !important;
  line-height: 1.35;

  * {
    box-sizing: border-box;
  }

  ul {
    padding-left: 0;
  }
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  min-height: $default-boxh;
  padding: 10px 2px;
  text-align: center;

  > span {
    @include font-size(18);

    display: block;

    &.link {
      @include font-size(12);

      display: flex;
      flex-wrap: wrap;
      justify-content: space-around;
      width: 100%;
      margin: 4px;
      margin-top: 16px;
      // font-size: 1.2rem;
      text-align: right;

      > a {
        width: 49.5%;
      }
    }

    &:not(:last-child) {
      overflow-wrap: break-word;
    }
  }

  span strong {
    @include font-size(20);
  }

  span.unit {
    @include font-size(18);
  }
}

.additionalData {
  font-size: 0.8em;

  span.delta::before {
    content: '(';
  }

  span.unit::after {
    content: ' )';
  }
}
</style>
<style lang="scss">
table.ibkCoronaNext {
  @include font-size(14);

  margin-bottom: 12px;

  th {
    font-weight: 400;
  }

  td {
    width: calc(100% / 6);
    text-align: center;
  }

  &.stageTable {
    &,
    tbody,
    tr {
      width: 100%;
    }

    td {
      &:nth-child(1) {
        width: 50px;
        height: fit-content;
        text-align: right;
      }

      &:nth-child(2) {
        width: 70px;
        text-align: left;
      }

      &:nth-child(3) {
        width: fit-content;
        text-align: left;
      }
    }
  }
}

span.stageMark {
  display: inline-block;
  width: 16px;
  height: 16px;
  margin: 0 0.5rem 0 0;
  vertical-align: middle;
  border: 0.5px solid #aaa;
  border-radius: 8px;

  &.MarkSmall {
    margin: 0;
    transform: scale(0.75);
  }

  &.stage1 {
    background-color: #cff;
  }

  &.stage2 {
    background-color: #ff6;
  }

  &.stage3 {
    background-color: #f93;
  }

  &.stage4 {
    background-color: #f00;
  }
}
</style>
