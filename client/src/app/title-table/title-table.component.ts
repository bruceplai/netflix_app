import { Component, OnInit, ViewChild } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { ITitle } from '../title';
import { TitleService } from '../title.service';
import {
  animate,
  state,
  style,
  transition,
  trigger,
} from '@angular/animations';

@Component({
  selector: 'title-table',
  templateUrl: './title-table.component.html',
  styleUrls: ['./title-table.component.scss'],
  animations: [
    trigger('detailExpand', [
      state('collapsed', style({ height: '0', minHeight: '0' })),
      state('expanded', style({ height: '*' })),
      transition(
        'expanded <=> collapsed',
        animate('225ms cubic-bezier(0.4, 0.0, 0.2, 1)')
      ),
    ]),
  ],
})
export class TitleTableComponent implements OnInit {
  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  public title = 'netflix';
  public displayedColumns: string[] = [
    'title',
    'type',
    'genre',
    'director',
    'castList',
  ];

  public dataSource = new MatTableDataSource<ITitle>();
  public expandedTitle: ITitle | null;

  constructor(private titleService: TitleService) {}

  private getData(): void {
    this.titleService.getTitles().subscribe((response) => {
      this.dataSource.paginator = this.paginator;
      this.dataSource.sort = this.sort;
      this.dataSource.data = response;
    });
  }

  public doFilter(value: string): void {
    this.dataSource.filter = value.trim().toLocaleLowerCase();
  }

  ngOnInit() {
    this.getData();
  }
}
