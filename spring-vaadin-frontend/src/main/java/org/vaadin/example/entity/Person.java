package org.vaadin.example.entity;

import java.util.Objects;
import java.util.concurrent.atomic.AtomicLong;

public class Person {
	
	private final static AtomicLong idCnt = new AtomicLong();
	
	private long id;
	private String name;
	private int age;

	public Person(String name, int age) {
		this(idCnt.incrementAndGet(), name, age);
	}
	
	public Person(long id, String name, int age) {
		this.id = id;
		this.name = name;
		this.age = age;
	}

	public long getId() {
		return id;
	}
	
	public String getName() {
		return name;
	}

	public int getAge() {
		return age;
	}
	
	@Override
	public String toString() {
		return id + "," + name + "," + age;
	}

	@Override
	public int hashCode() {
		return Objects.hash(id);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Person other = (Person) obj;
		return id == other.id;
	}
}