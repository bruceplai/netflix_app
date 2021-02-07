import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { ITitle } from './title';
import { IDataPoint } from './data-point';
import { Observable } from 'rxjs';

const API_BASE = 'http://localhost:9090';

@Injectable({ providedIn: 'root' })
export class TitleService {
  constructor(private http: HttpClient) {}

  private generateParams(
    title: string = null,
    director: string = null,
    actor: string = null
  ): HttpParams {
    let params = new HttpParams();
    if (title) {
      params = params.append('title', title);
    }
    if (director) {
      params = params.append('director', director);
    }
    if (actor) {
      params = params.append('actor', actor);
    }
    return params;
  }

  public getTitles(
    title: string = null,
    director: string = null,
    actor: string = null
  ): Observable<ITitle[]> {
    const params = this.generateParams(title, director, actor);
    return this.http.get<ITitle[]>(API_BASE + '/title', { params: params });
  }

  public getTitle(id: string): Observable<ITitle> {
    const params = new HttpParams({ fromObject: { id: id } });
    return this.http.get<ITitle>(API_BASE + '/title', { params: params });
  }

  public getYears(
    title: string = null,
    director: string = null,
    actor: string = null
  ): Observable<IDataPoint[]> {
    const params = this.generateParams(title, director, actor);
    return this.http.get<IDataPoint[]>(API_BASE + '/year', { params: params });
  }

  public getRatings(
    title: string = null,
    director: string = null,
    actor: string = null
  ): Observable<IDataPoint[]> {
    const params = this.generateParams(title, director, actor);
    return this.http.get<IDataPoint[]>(API_BASE + '/rating', { params: params });
  }

  public getGenres(
    title: string = null,
    director: string = null,
    actor: string = null
  ): Observable<IDataPoint[]> {
    const params = this.generateParams(title, director, actor);
    return this.http.get<IDataPoint[]>(API_BASE + '/genre', { params: params });
  }

  public getCountries(
    title: string = null,
    director: string = null,
    actor: string = null
  ): Observable<IDataPoint[]> {
    const params = this.generateParams(title, director, actor);
    return this.http.get<IDataPoint[]>(API_BASE + '/country', { params: params });
  }
}
