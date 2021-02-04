import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ITitle } from './title';
import { Observable } from 'rxjs';

const API_BASE = 'http://localhost:9090/';

@Injectable({ providedIn: 'root' })
export class TitleService {
  constructor(private http: HttpClient) {}

  public getTitles(): Observable<ITitle[]> {
    return this.http.get<ITitle[]>(API_BASE + 'titles');
  }

  public getTitle(id: string): Observable<ITitle> {
    return this.http.get<ITitle>(API_BASE + 'title' + id);
  }
}