import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Note } from './note';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class RestServiceService {

  constructor(private client: HttpClient) { }

  baseUrl = environment.baseUrl;


  public getNotes(): Observable<Note[]> {
    return this.client.get<Note[]>(`${this.baseUrl}`);
  }
}
