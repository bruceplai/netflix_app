import { Component, Input } from '@angular/core';
import { IDataPoint } from '../data-point';

@Component({
  selector: 'chart',
  templateUrl: './chart.component.html',
  styleUrls: ['./chart.component.scss']
})
export class ChartComponent {
  @Input() chartLabel: string;
  @Input() chartData: IDataPoint;

  showXAxis = true;
  showYAxis = true;
  gradient = false;
  showLegend = false;
  showXAxisLabel = true;
  showYAxisLabel = true;
  rotateXAxisTicks = true;
}
