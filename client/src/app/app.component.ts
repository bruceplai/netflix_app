import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatTableDataSource } from '@angular/material/table';
import { ITitle } from './title';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  private apiBase = 'http://localhost:9090/';

  title = 'netflix';
  displayedColumns: string[] = ['title', 'rating', 'director'];

  dataSource = new MatTableDataSource<ITitle>();

  constructor(private http: HttpClient) {}

  private getData() {
    this.http.get<ITitle[]>(this.apiBase + 'titles').subscribe(response => {
      console.log(response);
      this.dataSource.data = response;
    });
  }

  ngOnInit() {
    this.getData();
  }
}
