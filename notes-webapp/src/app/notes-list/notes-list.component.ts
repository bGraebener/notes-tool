import { Component, OnInit } from '@angular/core';
import { RestServiceService } from '../rest-service.service';
import { Note } from '../note';

@Component({
  selector: 'app-notes-list',
  templateUrl: './notes-list.component.html',
  styleUrls: ['./notes-list.component.css']
})
export class NotesListComponent implements OnInit {

  constructor(private rest: RestServiceService) { }

  notesList: Note[];

  ngOnInit() {
    this.rest.getNotes().subscribe((data: Note[]) => {
      this.notesList = data as Note[];
      this.notesList.forEach(note => {note.dateTime = new Date(note.dateTime); });
      console.log(data);
      console.log(typeof data[0].dateTime);

    });
  }

}
