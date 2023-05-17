using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ChaseCameraH : MonoBehaviour
{
    Vector3 base_pos;

    private void Start()
    {
        base_pos = Camera.main.gameObject.transform.position;
    }

    private void LateUpdate()
    {
        Vector3 pos = this.transform.position;
        pos.z = -10;
        pos.y = base_pos.y;
        Camera.main.gameObject.transform.position = pos;
    }
}
