import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FlexModule } from '@angular/flex-layout';
import { TruncatePipe } from './truncate.pipe';
import { ReplaceEmpty } from './replace-empty.pipe';
import { TitleTableComponent } from './title-table/title-table.component';
import { TitleDetailComponent } from './title-table/title-detail/title-detail.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { FormsModule } from '@angular/forms';
import { ChartComponent } from './chart/chart.component';
import { MaterialModule } from './material/material.module';
import { NgxChartsModule } from '@swimlane/ngx-charts';

@NgModule({
  declarations: [
    AppComponent,
    TruncatePipe,
    ReplaceEmpty,
    TitleTableComponent,
    TitleDetailComponent,
    DashboardComponent,
    ChartComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    FlexModule,
    FormsModule,
    MaterialModule,
    NgxChartsModule,
    RouterModule.forRoot([
      { path: 'search', component: TitleTableComponent },
      { path: 'stats', component: DashboardComponent },
      { path: '', redirectTo: 'search', pathMatch: 'full' },
      { path: '**', redirectTo: 'search', pathMatch: 'full' },
    ]),
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
