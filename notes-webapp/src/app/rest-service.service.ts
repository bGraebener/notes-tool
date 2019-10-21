import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import { Note } from './note';

@Injectable({
  providedIn: 'root'
})
export class RestServiceService {

  constructor(private client: HttpClient) { }

  baseUrl = 'http://localhost:5000/notes';


  public getNotes(): Observable<Note[]> {
    return this.client.get<Note[]>(`${this.baseUrl}`);
  }
}
