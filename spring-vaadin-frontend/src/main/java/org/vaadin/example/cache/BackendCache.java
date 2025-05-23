package org.vaadin.example.cache;

import java.time.Instant;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.vaadin.example.entity.CondolenceEntry;
import org.vaadin.example.entity.Person;

public class BackendCache {

	private final static Map<Long, Person> personCache = new HashMap<>();
	private final static Map<Person, List<CondolenceEntry>> condolenceCache = new HashMap<>();
	
	static {
		Person person = new Person("Gerda Müller", 78);
		personCache.put(person.getId(), person);
		List<CondolenceEntry> entries = new ArrayList<>();
		entries.add(new CondolenceEntry("Bryan Adams", Instant.now(), "The summer '69 was such a great memory."));
		condolenceCache.put(person, entries);
		person = new Person("Herbert Müller", 64);
		personCache.put(person.getId(), person);
	}
	
	public static Map<Long, Person> getPersonCache() {
		return personCache;
	}

	public static Map<Person, List<CondolenceEntry>> getCondolenceCache() {
		return condolenceCache;
	}
	
	public static List<CondolenceEntry> resolveFromPersonId(Long id) {
		Person person = personCache.get(id);
		if (person == null) {
			return Collections.emptyList();
		}
		List<CondolenceEntry> list = condolenceCache.get(person);
		if (list == null) {
			return Collections.emptyList();
		}
		return list;
	}
}
