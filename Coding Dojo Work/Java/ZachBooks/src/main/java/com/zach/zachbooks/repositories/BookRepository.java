package com.zach.zachbooks.repositories;

import java.util.List;

import com.zach.zachbooks.models.Book;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface BookRepository extends CrudRepository<Book, Long> {
    List<Book> findAll();

}
