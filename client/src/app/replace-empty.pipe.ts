import { Pipe, PipeTransform } from '@angular/core';

@Pipe({ name: 'replaceEmpty' })
export class ReplaceEmpty implements PipeTransform {
  transform(value: string) {
    return value || 'N/A';
  }
}
