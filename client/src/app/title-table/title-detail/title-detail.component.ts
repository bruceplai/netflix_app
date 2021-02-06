import { Component, Input } from '@angular/core';
import { ITitle } from 'src/app/title';

@Component({
  selector: 'title-detail',
  templateUrl: './title-detail.component.html',
  styleUrls: ['./title-detail.component.scss'],
})
export class TitleDetailComponent {
  @Input() title: ITitle;
}
