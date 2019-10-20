import { Component, OnInit } from '@angular/core';
import { RestServiceService } from '../rest-service.service';

@Component({
  selector: 'app-notes-list',
  templateUrl: './notes-list.component.html',
  styleUrls: ['./notes-list.component.css']
})
export class NotesListComponent implements OnInit {

  constructor(private rest:RestServiceService) { }

  notesList = {};
  ngOnInit() {
    this.rest.getNotes().subscribe((data:{})=> {
      this.notesList = data;
      console.log(data);

    })
  }

}
